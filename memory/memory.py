from pathlib import Path
import sqlite3
from datetime import datetime


DB_PATH = Path(__file__).parent / "memory.db"


class Memory:

    def __init__(self):

        DB_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.conn = sqlite3.connect(DB_PATH)

        self.conn.row_factory = sqlite3.Row

        self.create()

    def create(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            role TEXT,

            content TEXT

        )
        """)

        self.conn.commit()

    def add(self, role, content):

        cursor = self.conn.cursor()

        cursor.execute(

            """
            INSERT INTO messages(
                timestamp,
                role,
                content
            )
            VALUES(?,?,?)
            """,

            (
                datetime.now().isoformat(),
                role,
                content
            )

        )

        self.conn.commit()

    def conversation(self, limit=20):

        cursor = self.conn.cursor()

        cursor.execute(

            """
            SELECT *
            FROM messages
            ORDER BY id DESC
            LIMIT ?
            """,

            (limit,)

        )

        rows = cursor.fetchall()

        return list(reversed([
            dict(row)
            for row in rows
        ]))

    def search(self, text):

        cursor = self.conn.cursor()

        cursor.execute(

            """
            SELECT *
            FROM messages
            WHERE content LIKE ?
            ORDER BY id DESC
            """,

            (f"%{text}%",)

        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    def clear(self):

        cursor = self.conn.cursor()

        cursor.execute(
            "DELETE FROM messages"
        )

        self.conn.commit()

    def count(self):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM messages"
        )

        return cursor.fetchone()[0]


memory = Memory()
