
from lib.models.author import Author

def test_author_creation():
    author = Author("J.K. Rowling")
    author.save()
    assert author.id is not None
    assert author.name == "J.K. Rowling"