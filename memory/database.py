import sqlite3
from pathlib import Path


DB_FOLDER = Path("memory")
DB_FOLDER.mkdir(exist_ok=True)

DB_PATH = DB_FOLDER / "memory.db"


class MemoryDatabase:

    def __init__(self):

        self.connection = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row

        self.create_tables()

    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user TEXT NOT NULL,

                assistant TEXT NOT NULL,

                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
        """)

        self.connection.commit()

    def save(self, user, assistant):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO messages(user, assistant)
            VALUES (?, ?)
            """,
            (user, assistant)
        )

        self.connection.commit()

    def recent(self, limit=10):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT user, assistant
            FROM messages
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        rows = cursor.fetchall()

        return list(reversed(rows))

    def clear(self):

        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM messages")

        self.connection.commit()

    def count(self):

        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM messages"
        )

        return cursor.fetchone()[0]

    def close(self):

        self.connection.close()


database = MemoryDatabase()
