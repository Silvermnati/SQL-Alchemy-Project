# lib/models/article.py
from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title  # This will trigger the setter
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id:
                cursor.execute("""
                    UPDATE articles 
                    SET title = ?, author_id = ?, magazine_id = ? 
                    WHERE id = ?
                """, (self.title, self.author_id, self.magazine_id, self.id))
            else:
                cursor.execute("""
                    INSERT INTO articles (title, author_id, magazine_id) 
                    VALUES (?, ?, ?)
                """, (self.title, self.author_id, self.magazine_id))
                self.id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()
        return self

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return cls(row['title'], row['author_id'], row['magazine_id'], row['id'])
            return None
        finally:
            conn.close()

    def author(self):
        from lib.models.author import Author
        return Author.find_by_id(self.author_id)

    def magazine(self):
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)