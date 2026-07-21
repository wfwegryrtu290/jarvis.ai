import sqlite3

from workspace.database import DB


def find_symbol(name):

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute(

        """
        SELECT
            file,
            type,
            line
        FROM symbols
        WHERE name=?
        """,

        (name,)

    )

    rows = cur.fetchall()

    conn.close()

    return rows