from sqlite_utils import Database
from pathlib import Path

def check_database():
    db_path = Path('data.sqlite')
    if not db_path.exists():
        print("Database file not found!")
        return
    
    db = Database(db_path)
    print('Tables in database:')
    for table in db.tables:
        print(f'\nTable: {table}')
        print('Schema:')
        print(db[table].schema)

if __name__ == "__main__":
    check_database()
