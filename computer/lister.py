from pathlib import Path

from computer.search import search
from context.context import context


def list_folder(target=None):

    if target is None:

        path = context.current_folder

        if not path:

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

        for item in sorted(folder.iterdir(), key=lambda x: x.name.lower()):

            if item.is_dir():

                folders.append(item.name)

            else:

                files.append(item.name)

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    context.current_folder = str(folder)

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
