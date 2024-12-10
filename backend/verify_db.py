from app.database import init_db, get_schema

def verify_database():
    # Initialize the database
    init_db()

    # Get and print schema
    schema = get_schema()
    print("Database Schema:")
    for table_name, table_sql in schema.items():
        print(f"\n{table_name} table:")
        print(table_sql)

if __name__ == "__main__":
    verify_database()
