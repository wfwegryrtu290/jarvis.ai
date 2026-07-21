import sqlite3

DB = "developer/developer.db"


def create():

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute("""

    CREATE TABLE IF NOT EXISTS fixes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        file TEXT,

        error TEXT,

        fix TEXT,

        success INTEGER

    )

    """)

    conn.commit()
    conn.close()


def save(file, error, fix, success):

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute(

        "INSERT INTO fixes(file,error,fix,success) VALUES(?,?,?,?)",

        (file, error, fix, success)

    )

    conn.commit()
    conn.close()


def history():

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute("SELECT * FROM fixes ORDER BY id DESC LIMIT 20")

    rows = cur.fetchall()

    conn.close()

    return rows