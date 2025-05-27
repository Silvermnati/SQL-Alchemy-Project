from lib.db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

    def save(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            if self.id:
                cursor.execute("UPDATE authors SET name=? WHERE id=?", 
                             (self.name, self.id))
            else:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", 
                             (self.name,))
                self.id = cursor.lastrowid
            conn.commit()
        return self

    @classmethod
    def find_by_id(cls, author_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE id=?", (author_id,))
            row = cursor.fetchone()
            return cls(row['name'], row['id']) if row else None

    