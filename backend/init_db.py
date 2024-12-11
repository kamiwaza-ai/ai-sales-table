import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        conn = sqlite3.connect('data.db')
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_tables(conn):
    try:
        cursor = conn.cursor()

        # Create columns table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS columns (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            extraction_key TEXT NOT NULL UNIQUE
        )
        """)

        # Create rows table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rows (
            id TEXT PRIMARY KEY,
            website TEXT NOT NULL,
            data TEXT NOT NULL
        )
        """)

        conn.commit()
        print("Database tables created successfully")
    except Error as e:
        print(f"Error creating tables: {e}")

def main():
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
        conn.close()
    else:
        print("Error: Could not create database connection")

if __name__ == "__main__":
    main()
