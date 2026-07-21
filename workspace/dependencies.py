import sqlite3

from workspace.database import DB


def get_dependencies(file):

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute(

        "SELECT module FROM imports WHERE file=?",

        (file,)

    )

    rows = cur.fetchall()

    conn.close()

    return [r[0] for r in rows]