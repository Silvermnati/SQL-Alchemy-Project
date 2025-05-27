-- lib/db/schema.sql
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) > 0)
);

CREATE TABLE magazines (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) > 0),
    category TEXT NOT NULL CHECK(length(category) > 0)
);

CREATE TABLE articles (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL CHECK(length(title) BETWEEN 5 AND 50),
    author_id INTEGER NOT NULL,
    magazine_id INTEGER NOT NULL,
    FOREIGN KEY(author_id) REFERENCES authors(id),
    FOREIGN KEY(magazine_id) REFERENCES magazines(id)
);

CREATE INDEX idx_articles_author ON articles(author_id);
CREATE INDEX idx_articles_magazine ON articles(magazine_id);