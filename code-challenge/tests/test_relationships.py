from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_author_magazine_relationship():
    # Create and save author
    author = Author("Ernest Hemingway")
    author.save()
    print(f"Author ID: {author.id}")
    
    # Create and save magazine
    magazine = Magazine("Literary Digest", "Literature")
    magazine.save()
    print(f"Magazine ID: {magazine.id}")
    
    # Create and save article
    article = Article("Old Man and the Sea", author.id, magazine.id)
    article.save()
    print(f"Article ID: {article.id}")
    
    # Test relationships
    author_magazines = author.magazines()
    print(f"Author magazines: {author_magazines}")
    
    magazine_contributors = magazine.contributors()
    print(f"Magazine contributors: {magazine_contributors}")
    
    assert magazine in author_magazines, \
        f"Expected {magazine} in author's magazines, but found {author_magazines}"
    
    assert author in magazine_contributors, \
        f"Expected {author} in magazine contributors, but found {magazine_contributors}"