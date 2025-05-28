from lib.db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"
    
    def __eq__(self, other):
        return isinstance(other, Author) and self.id == other.id
    
    def __hash__(self):
        return hash(self.id)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id:
                cursor.execute(
                    "UPDATE authors SET name = ? WHERE id = ?", 
                    (self.name, self.id)
                )
            else:
                cursor.execute(
                    "INSERT INTO authors (name) VALUES (?)", 
                    (self.name,)
                )
                self.id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()
        return self

    @classmethod
    def find_by_id(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
            row = cursor.fetchone()
            if row:
                return cls(row['name'], row['id'])
            return None
        finally:
            conn.close()

    def magazines(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT DISTINCT magazines.* FROM magazines
                JOIN articles ON magazines.id = articles.magazine_id
                WHERE articles.author_id = ?
            """, (self.id,))
            rows = cursor.fetchall()
            return [Magazine(row['name'], row['category'], row['id']) for row in rows]
        finally:
            conn.close()