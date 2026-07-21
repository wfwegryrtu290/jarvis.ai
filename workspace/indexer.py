import sqlite3

from workspace.database import DB
from workspace.parser import parse_python


def index_python(path):

    parsed = parse_python(path)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # Изчистваме старите записи за този файл
    cur.execute("DELETE FROM symbols WHERE file=?", (path,))
    cur.execute("DELETE FROM imports WHERE file=?", (path,))

    # Функции
    for f in parsed["functions"]:

        cur.execute(
            "INSERT INTO symbols(file,type,name,line) VALUES(?,?,?,?)",
            (
                path,
                "function",
                f["name"],
                f["line"]
            )
        )

    # Класове
    for c in parsed["classes"]:

        cur.execute(
            "INSERT INTO symbols(file,type,name,line) VALUES(?,?,?,?)",
            (
                path,
                "class",
                c["name"],
                c["line"]
            )
        )

    # Импорти
    for imp in parsed["imports"]:

        cur.execute(
            "INSERT INTO imports(file,module) VALUES(?,?)",
            (
                path,
                imp
            )
        )

    conn.commit()
    conn.close()


def index_workspace(files):
    """
    Индексира всички Python файлове от резултата на scanner.py
    """

    for file in files:

        path = file["path"]

        if path.lower().endswith(".py"):

            try:
                index_python(path)
            except Exception as e:
                print(f"❌ Грешка при индексиране на {path}: {e}")