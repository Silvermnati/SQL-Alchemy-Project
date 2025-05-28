# tests/test_relationships.py
def test_author_magazine_relationship():
    author = Author("Ernest Hemingway").save()
    magazine = Magazine("Literary Digest", "Literature").save()
    
    article = Article("Old Man and the Sea", author.id, magazine.id).save()
    
    assert magazine in author.magazines()
    assert author in magazine.contributors()