from pathlib import Path

from core.logger import logger
from computer.index import computer


HOME = Path.home()

SPECIAL_FOLDERS = {
    "desktop": HOME / "Desktop",
    "documents": HOME / "Documents",
    "downloads": HOME / "Downloads",
    "pictures": HOME / "Pictures",
    "videos": HOME / "Videos",
    "music": HOME / "Music",
}


def score(kind, path):

    p = str(path).lower()

    value = 0

    # Потребителските файлове имат най-висок приоритет
    if str(HOME).lower() in p:
        value += 1000

    priorities = {
        "desktop": 900,
        "documents": 800,
        "downloads": 700,
        "pictures": 600,
        "videos": 500,
        "music": 400,
    }

    for folder, points in priorities.items():

        if folder in p:
            value += points

    if kind == "app":

        if p.endswith(".exe"):
            value += 5000

        elif p.endswith(".lnk"):
            value += 2500

        else:
            value += 1000

        if "program files" in p:
            value += 800

    return value


def add_result(results, kind, name, path, target, exact_bonus):

    if name == target:

        results.append(
            (
                kind,
                path,
                exact_bonus + score(kind, path),
            )
        )

        return

    if target in name:

        results.append(
            (
                kind,
                path,
                score(kind, path),
            )
        )


def search_apps(target, results):

    for name, path in computer.apps.items():

        add_result(
            results,
            "app",
            name,
            path,
            target,
            100000,
        )


def search_files(target, results):

    for name, path in computer.files.items():

        add_result(
            results,
            "file",
            name,
            path,
            target,
            30000,
        )


def search_folders(target, results):

    for name, path in computer.folders.items():

        add_result(
            results,
            "folder",
            name,
            path,
            target,
            10000,
        )


def sort_results(results):

    results.sort(
        key=lambda item: item[2],
        reverse=True,
    )

    return results
    def search(target):

    if not target:
        return None

    target = target.lower().strip()

    logger.debug(f"Searching for: {target}")

    # ==========================
    # Special folders
    # ==========================

    if target in SPECIAL_FOLDERS:

        folder = SPECIAL_FOLDERS[target]

        if folder.exists():

            logger.debug(f"Found special folder: {folder}")

            return (
                "folder",
                str(folder)
            )

    # ==========================
    # Search
    # ==========================

    results = []

    search_apps(
        target,
        results
    )

    search_files(
        target,
        results
    )

    search_folders(
        target,
        results
    )

    # ==========================
    # Nothing found
    # ==========================

    if not results:

        logger.debug("Nothing found.")

        return None

    # ==========================
    # Sort
    # ==========================

    sort_results(results)

    kind, path, score_value = results[0]

    logger.debug(
        f"Found {kind}: {path} ({score_value})"
    )

    return (
        kind,
        path
    )


def search_all(target):

    """
    Връща всички резултати,
    сортирани по приоритет.
    """

    if not target:

        return []

    target = target.lower().strip()

    results = []

    search_apps(
        target,
        results
    )

    search_files(
        target,
        results
    )

    search_folders(
        target,
        results
    )

    if not results:

        return []

    return sort_results(results)


def exists(target):

    return search(target) is not None
