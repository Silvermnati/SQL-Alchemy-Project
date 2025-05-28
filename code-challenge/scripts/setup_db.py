import os
import sys
from pathlib import Path
import sqlite3

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

def initialize_database():
    db_file = 'articles.db'
    
    # Remove existing database file
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Removed existing database: {db_file}")
    
    # Create new database
    conn = sqlite3.connect(db_file)
    try:
        # Read schema file
        schema_path = Path(__file__).parent.parent / 'lib' / 'db' / 'schema.sql'
        with open(schema_path, 'r') as f:
            schema = f.read()
        
        # Execute schema commands
        conn.executescript(schema)
        conn.commit()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
    finally:
        conn.close()

if __name__ == '__main__':
    initialize_database()