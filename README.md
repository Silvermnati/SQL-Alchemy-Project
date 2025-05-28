# Magazine Article System

A Python/SQLite system for managing relationships between authors, articles, and magazines.

## Features
- Author management (create, update)
- Magazine management (create, update)
- Article management with relationships
- SQL queries for complex relationships
- Transaction support

## Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install pytest

# Initialize database
python scripts/setup_db.py

# Run all tests
pytest tests/

# Run specific test with debug output
pytest tests/test_relationships.py -v -s

code-challenge/
├── lib/              # Core application code
│   ├── models/       # Database models (Author, Article, Magazine)
│   └── db/           # Database connection and schema
├── tests/            # Test cases
├── scripts/          # Utility scripts
└── articles.db       # SQLite database (auto-generated)

# Create author
from lib.models.author import Author
author = Author("J.K. Rowling").save()

# Create magazine
from lib.models.magazine import Magazine
magazine = Magazine("Literary Review", "Fiction").save()

# Create article
from lib.models.article import Article
article = Article("Harry Potter", author.id, magazine.id).save()

# Get author's magazines
print(author.magazines())

# Get magazine's contributors
print(magazine.contributors())

Copyright (c) [2024] [MNATI PUBLISHERS]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.