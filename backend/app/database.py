import sqlite3
import json
from contextlib import contextmanager
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / "data.sqlite"

@contextmanager
def get_db():
    conn = sqlite3.connect(str(DATABASE_PATH))
    try:
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.execute("DROP TABLE IF EXISTS columns")
        conn.execute("DROP TABLE IF EXISTS rows")
        conn.execute("""
            CREATE TABLE columns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
        """)
        conn.execute("""
            CREATE TABLE rows (
                id TEXT PRIMARY KEY,
                website TEXT NOT NULL,
                data TEXT NOT NULL,
                CONSTRAINT ensure_json CHECK (json_valid(data))
            )
        """)
        conn.commit()

def get_schema():
    with get_db() as conn:
        tables = conn.execute("""
            SELECT name, sql FROM sqlite_master
            WHERE type='table' AND name IN ('columns', 'rows')
        """).fetchall()
        return {table['name']: table['sql'] for table in tables}
