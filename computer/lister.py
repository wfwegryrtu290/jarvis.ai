from pathlib import Path

from computer.history import history
from computer.search import search


def list_folder(target=None):

    # Ако не е подадена папка, използвай последната отворена
    if target is None:

        path = history.last_folder

        if path is None:

            return {
                "success": False,
                "error": "Няма избрана папка."
            }

    else:

        result = search(target)

        if result is None:

            return {
                "success": False,
                "error": f"Не намерих '{target}'."
            }

        kind, path = result

        if kind != "folder":

            return {
                "success": False,
                "error": f"'{target}' не е папка."
            }

    folder = Path(path)

    if not folder.exists():

        return {
            "success": False,
            "error": "Папката не съществува."
        }

    folders = []
    files = []

    try:

        for item in sorted(folder.iterdir()):

            if item.is_dir():
                folders.append(item.name)
            else:
                files.append(item.name)

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    history.remember("folder", str(folder))

    return {

        "success": True,

        "report": {
            "path": str(folder),
            "folders": folders,
            "files": files,
            "folder_count": len(folders),
            "file_count": len(files)
        }

    }