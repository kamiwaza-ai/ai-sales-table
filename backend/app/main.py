from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
import json
from typing import List, Dict

from .models import Column, Row, ColumnCreate, RowCreate
from .database import get_db
from .firecrawl import extract_data

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: Dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                print(f"Error broadcasting to client: {e}")

manager = ConnectionManager()
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
async def get_data():
    """Retrieve current state of the grid"""
    with get_db() as conn:
        columns = conn.execute("SELECT * FROM columns").fetchall()
        rows = conn.execute("SELECT * FROM rows").fetchall()

        return {
            "columns": [
                {"id": col["id"], "name": col["name"]}
                for col in columns
            ],
            "rows": [
                {"id": row["id"], "website": row["website"], "data": json.loads(row["data"])}
                for row in rows
            ]
        }

@app.post("/api/columns")
async def add_column(column: ColumnCreate):
    """Add a new column to extract and trigger extraction for all rows"""
    try:
        with get_db() as conn:
            # Check if column with same name already exists
            existing = conn.execute(
                "SELECT * FROM columns WHERE name = ?",
                (column.name,)
            ).fetchone()

            if existing:
                raise HTTPException(status_code=400, detail="Column with this name already exists")

            # Create column
            column_id = str(uuid4())

            # Add new column
            conn.execute(
                "INSERT INTO columns (id, name) VALUES (?, ?)",
                (column_id, column.name)
            )

            conn.commit()

            # Broadcast update to all connected clients
            updated_data = await get_data()
            await manager.broadcast({"type": "update", "data": updated_data})

            return {"message": "Column added successfully", "id": column_id}
    except Exception as e:
        print(f"Error adding column: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/rows")
async def add_row(row: RowCreate):
    """Add a new website to extract data from"""
    print(f"Received request to add row with website: {row.website}")
    try:
        with get_db() as conn:
            # Check if any columns exist first
            columns = conn.execute("SELECT COUNT(*) as count FROM columns").fetchone()
            if columns['count'] == 0:
                print("No columns exist, skipping row addition")
                return {"message": "No columns exist yet"}

            # Create row
            row_id = str(uuid4())
            print(f"Generated row ID: {row_id}")

            # Add new row with empty data
            conn.execute(
                "INSERT INTO rows (id, website, data) VALUES (?, ?, ?)",
                (row_id, row.website, json.dumps({}))
            )
            conn.commit()
            print(f"Successfully added row with ID: {row_id}")

            # Broadcast update to all connected clients
            updated_data = await get_data()
            await manager.broadcast({"type": "update", "data": updated_data})

            return {"message": "Row added successfully", "id": row_id}
    except Exception as e:
        print(f"Error adding row: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/refresh")
async def refresh_data():
    """Trigger extraction for all rows"""
    try:
        print("\n=== Starting refresh_data operation ===")
        with get_db() as conn:
            # Get all columns
            columns = [
                Column(**col)
                for col in conn.execute("SELECT * FROM columns").fetchall()
            ]
            print(f"Found columns: {[col.name for col in columns]}")

            if not columns:
                print("No columns defined for extraction")
                return {"message": "No columns defined for extraction"}

            # Get all rows
            rows = conn.execute("SELECT id, website FROM rows").fetchall()
            print(f"Found rows: {[row['website'] for row in rows]}")

            # Process each row
            for row in rows:
                try:
                    print(f"\nProcessing row for website: {row['website']}")
                    extracted_data = await extract_data(row["website"], columns)
                    print(f"Extracted data: {extracted_data}")

                    conn.execute(
                        "UPDATE rows SET data = ? WHERE id = ?",
                        (json.dumps(extracted_data), row["id"])
                    )
                    print(f"Updated row {row['id']} with extracted data")
                except Exception as e:
                    print(f"Error extracting data for {row['website']}: {e}")
                    # Set N/A for all columns on error
                    error_data = {col.name: "N/A" for col in columns}
                    print(f"Setting error data: {error_data}")
                    conn.execute(
                        "UPDATE rows SET data = ? WHERE id = ?",
                        (json.dumps(error_data), row["id"])
                    )

            conn.commit()
            print("Database changes committed")

            # Broadcast update to all connected clients
            updated_data = await get_data()
            print(f"Broadcasting updated data: {updated_data}")
            await manager.broadcast({"type": "update", "data": updated_data})
            print("=== Refresh operation completed ===\n")

            return {"message": "Data refreshed successfully"}
    except Exception as e:
        print(f"Error refreshing data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/columns")
async def clear_columns():
    """Clear all columns and associated row data"""
    with get_db() as conn:
        conn.execute("DELETE FROM columns")
        conn.execute("DELETE FROM rows")
        conn.commit()

        # Broadcast update to all connected clients
        updated_data = await get_data()
        await manager.broadcast({"type": "update", "data": updated_data})

        return {"message": "All columns cleared successfully"}

@app.websocket("/ws/updates")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time updates"""
    await manager.connect(websocket)
    try:
        # Send initial data
        data = await get_data()
        await websocket.send_json({"type": "update", "data": data})

        while True:
            # Keep connection alive and handle any incoming messages
            await websocket.receive_text()

    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        manager.disconnect(websocket)
