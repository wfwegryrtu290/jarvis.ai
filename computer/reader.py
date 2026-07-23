from pathlib import Path

from computer.search import search
from context.context import context


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

    # Ако няма подаден файл, използвай последния избран
    if target is None:

        path = context.current_file

        if not path:

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

    if not file.exists():

        return {
            "success": False,
            "error": "Файлът не съществува."
        }

    if file.suffix.lower() not in TEXT_EXTENSIONS:

        return {
            "success": False,
            "error": f"Форматът {file.suffix} все още не се поддържа."
        }

    try:

        text = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    context.current_file = str(file)

    return {

        "success": True,

        "report": text,

        "path": str(file)

    }
