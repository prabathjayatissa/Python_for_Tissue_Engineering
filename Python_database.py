"""Lession 3"""

import sqlite3

# connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    genre VARCHAR(50),
    year_published INTEGER
);
""")

conn.commit()
conn.close()

import sqlite3

def create_employee_table() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE employees (
            emp_id INTEGER,
            emp_name TEXT,
            department TEXT,
            salary REAL
        )
    """)
    conn.commit()
    return conn

    # Create table
conn = create_employee_table()
c = conn.cursor()

# Insert some sample data
employees = [
    (1, 'Prabath', 'CS', 90000),
    (2, 'Lilly', 'LS', 80000),
    (3, 'Charlie', 'HR', 55000)
]
c.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees)
conn.commit()

# Query and print the results
for row in c.execute("SELECT * FROM employees"):
    print(row)

import sqlite3

def create_books_table() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE books (
            isbn TEXT PRIMARY KEY,
            title TEXT,
            author TEXT
        )
    """)
    conn.commit()
    return conn

import sqlite3

def create_library_db() -> list[tuple]:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    # Create tables
    c.execute("""
        CREATE TABLE authors (
            author_id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    c.execute("""
        CREATE TABLE books (
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
        )
    """)

    # Insert data
    c.executemany("INSERT INTO authors (author_id, name) VALUES (?, ?)", [
        (1, 'George Orwell'),
        (2, 'Jane Austen')
    ])
    c.executemany("INSERT INTO books (book_id, title, author_id) VALUES (?, ?, ?)", [
        (1, '1984', 1),
        (2, 'Animal Farm', 1),
        (3, 'Pride and Prejudice', 2)
    ])

    # Query with JOIN
    c.execute("""
        SELECT books.title, authors.name
        FROM books
        JOIN authors ON books.author_id = authors.author_id
    """)
    return c.fetchall()

