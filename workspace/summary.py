import sqlite3

from workspace.database import DB


def project_summary():

    conn = sqlite3.connect(DB)

    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM files")
    files = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM symbols")
    symbols = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM imports")
    imports = cur.fetchone()[0]

    conn.close()

    return {

        "files": files,

        "symbols": symbols,

        "imports": imports

    }