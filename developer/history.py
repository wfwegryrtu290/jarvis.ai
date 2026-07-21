import sqlite3

DB = "developer/history.db"


def create():

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute("""

    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        file TEXT,

        prompt TEXT,

        answer TEXT

    )

    """)

    conn.commit()

    conn.close()


def save(file, prompt, answer):

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute(

        "INSERT INTO history(file,prompt,answer) VALUES(?,?,?)",

        (file, prompt, answer)

    )

    conn.commit()

    conn.close()