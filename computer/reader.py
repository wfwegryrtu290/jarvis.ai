from pathlib import Path

from computer.search import search
from computer.history import history


TEXT_EXTENSIONS = {
    ".txt",
    ".py",
    ".md",
    ".json",
    ".yaml",
    ".yml",
    ".ini",
    ".cfg",
    ".csv",
    ".log",
    ".xml",
    ".html",
    ".css",
    ".js"
}


def read_file(target=None):

    if target is None:

        path = history.last_file

        if path is None:
            return {
                "success": False,
                "error": "Няма избран файл."
            }

    else:

        result = search(target)

        if result is None:
            return {
                "success": False,
                "error": f"Не намерих '{target}'."
            }

        kind, path = result

        if kind != "file":
            return {
                "success": False,
                "error": "Това не е файл."
            }

    file = Path(path)

    if file.suffix.lower() not in TEXT_EXTENSIONS:

        return {
            "success": False,
            "error": "Форматът все още не се поддържа."
        }

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    history.remember("file", str(file))

    return {

        "success": True,

        "report": text,

        "path": str(file)

    }