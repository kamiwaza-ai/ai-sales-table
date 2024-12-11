import sqlite3
from pathlib import Path

def check_rows():
    db_path = Path(__file__).parent / "data.sqlite"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    print("\n=== Checking Database Contents ===")

    # Check columns
    print("\nColumns:")
    columns = conn.execute("SELECT * FROM columns").fetchall()
    for col in columns:
        print(f"- ID: {col['id']}, Name: {col['name']}")

    # Check rows
    print("\nRows:")
    rows = conn.execute("SELECT * FROM rows").fetchall()
    for row in rows:
        print(f"- ID: {row['id']}")
        print(f"  Website: {row['website']}")
        print(f"  Data: {row['data']}")

    conn.close()

if __name__ == "__main__":
    check_rows()
