import sqlite3

from aiogram.types import location
from src.responces import check_geo


def create_db():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            location TEXT,
            lat TEXT,
            lon TEXT
        )
        """)


def check_user_exists(id: str):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()

        cursor.execute("SELECT 1 FROM users WHERE id = ?", (id,))
        return cursor.fetchone() is not None


def append_user(id: str, location: str):
    if check_geo(location):
        result = check_geo(location)
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()

            cursor.execute(
                """
            INSERT INTO users (id, location, lat, lon)
            VALUES (?, ?, ?, ?)
            """,
                (id, result["ru_name"], result["lat"], result["lon"]),
            )
    else:
        return False


def get_location(id: str):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()

        cursor.execute("SELECT location FROM users WHERE id = ?", (id,))
        name = cursor.fetchone()[0]
        cursor.execute("SELECT lat FROM users WHERE id = ?", (id,))
        lat = cursor.fetchone()[0]
        cursor.execute("SELECT lon FROM users WHERE id = ?", (id,))
        lon = cursor.fetchone()[0]
        result = {"name": name, "lat": lat, "lon": lon}
        return result
