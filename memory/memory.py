import sqlite3

DB = "memory/memory.db"


def create_memory():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            assistant TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_message(user, assistant):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages(user, assistant) VALUES (?, ?)",
        (user, assistant)
    )

    conn.commit()
    conn.close()


def get_memory(limit=10):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user, assistant FROM messages ORDER BY id DESC LIMIT ?",
        (limit,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows[::-1]