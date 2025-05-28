# lib/debug.py
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def start_debug_session():
    print("=== DEBUG CONSOLE ===")
    print("Available classes: Author, Magazine, Article")
    import code
    code.interact(local=locals())

if __name__ == '__main__':
    start_debug_session()