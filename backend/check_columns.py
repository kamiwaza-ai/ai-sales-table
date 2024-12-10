import sqlite3

def check_columns():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Get all columns
    cursor.execute("SELECT * FROM columns")
    columns = cursor.fetchall()

    print("Current columns in database:")
    for column in columns:
        print(f"ID: {column[0]}, Name: {column[1]}, Extraction Key: {column[2]}")

    conn.close()

if __name__ == "__main__":
    check_columns()
