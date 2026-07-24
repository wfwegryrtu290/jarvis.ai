from pathlib import Path

from core.logger import logger
from computer.search import search
from context.context import context


def list_folder(target=None):

    # Използвай последната отворена папка
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

    logger.info(f"Listing folder: {folder}")

    folders = []
    files = []

    total_size = 0
    hidden_count = 0

    try:

        for item in sorted(folder.iterdir(), key=lambda x: x.name.lower()):

            if item.name.startswith("."):
                hidden_count += 1

            if item.is_dir():

                folders.append({
                    "name": item.name,
                    "path": str(item)
                })

            else:

                try:
                    size = item.stat().st_size
                except Exception:
                    size = 0

                total_size += size

                files.append({
                    "name": item.name,
                    "path": str(item),
                    "size": size,
                    "extension": item.suffix.lower()
                })

    except Exception as e:

        logger.exception(e)

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
            "file_count": len(files),
            "hidden_items": hidden_count,
            "total_size": total_size
        }
    }
