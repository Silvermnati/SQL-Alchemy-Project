import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from lib.db.connection import get_connection

def initialize_database():
    conn = get_connection()
    
    # Add this line to drop existing tables
    conn.executescript("""
        DROP TABLE IF EXISTS articles;
        DROP TABLE IF EXISTS authors;
        DROP TABLE IF EXISTS magazines;
    """)
    
    with open('lib/db/schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    print("Database reset and initialized!")
    
def initialize_database():
    conn = get_connection()
    with open('lib/db/schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    print("Database initialized!")

if __name__ == '__main__':
    initialize_database()