import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "test.db"


connection = sqlite3.connect(DB_PATH)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT
)
""")


cursor.execute("""
DELETE FROM users
""")


users = [
    (1, "George", "Bluth", "george@reqres.in"),
    (2, "Janet", "Weaver", "janet@reqres.in"),
    (3, "Emma", "Wong", "emma@reqres.in")
]


cursor.executemany(
    """
    INSERT INTO users
    (id, first_name, last_name, email)
    VALUES (?, ?, ?, ?)
    """,
    users
)


connection.commit()
connection.close()


print("Database created successfully.")
print(f"Database location: {DB_PATH}")