import sqlite3
from pathlib import Path

def clear_database():
    try:
        # Use the same database path as in database.py
        db_path = Path(__file__).parent / "data.sqlite"
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        # Drop existing tables
        cursor.execute("DROP TABLE IF EXISTS columns")
        cursor.execute("DROP TABLE IF EXISTS rows")

        # Create tables with same schema as database.py
        cursor.execute("""
        CREATE TABLE columns (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE rows (
            id TEXT PRIMARY KEY,
            website TEXT NOT NULL,
            data TEXT NOT NULL,
            CONSTRAINT ensure_json CHECK (json_valid(data))
        )
        """)

        conn.commit()
        print("Database cleared and tables recreated successfully")

        conn.close()
    except Exception as e:
        print(f"Error clearing database: {e}")

if __name__ == "__main__":
    clear_database()
