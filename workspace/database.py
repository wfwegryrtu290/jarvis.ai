import sqlite3

DB = "workspace/workspace.db"


def create():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS files(

        path TEXT PRIMARY KEY,
        name TEXT,
        extension TEXT,
        type TEXT,
        size INTEGER,
        modified REAL

    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS symbols(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        file TEXT,
        type TEXT,
        name TEXT,
        line INTEGER

    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS imports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        file TEXT,
        module TEXT

    )
    """)

    conn.commit()
    conn.close()


def add_file(file):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""

    INSERT OR REPLACE INTO files(

        path,
        name,
        extension,
        type,
        size,
        modified

    )

    VALUES(?,?,?,?,?,?)

    """, (

        file["path"],
        file["name"],
        file["extension"],
        file["type"],
        file["size"],
        file["modified"]

    ))

    conn.commit()
    conn.close()


def clear():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("DELETE FROM files")
    cur.execute("DELETE FROM symbols")
    cur.execute("DELETE FROM imports")

    conn.commit()
    conn.close()