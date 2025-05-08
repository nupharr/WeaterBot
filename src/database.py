import sqlite3
from src.responces import check_geo


def create_db():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            location TEXT
        )
        """)


def check_user_exists(id: str):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()

        cursor.execute("SELECT 1 FROM users WHERE id = ?", (id,))
        return cursor.fetchone() is not None


def append_user(id: str, location: str):
    if check_geo(location):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()

            cursor.execute(
                """
            INSERT INTO users (id, location)
            VALUES (?, ?)
            """,
                (id, location),
            )
    else:
        return None
