import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from lib.db.connection import get_connection

def initialize_database():
    conn = get_connection()
    with open('lib/db/schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    print("Database initialized!")

if __name__ == '__main__':
    initialize_database()