from pathlib import Path

from computer.index import computer


HOME = Path.home()

SPECIAL_FOLDERS = {

    "desktop": HOME / "Desktop",

    "documents": HOME / "Documents",

    "downloads": HOME / "Downloads",

    "pictures": HOME / "Pictures",

    "videos": HOME / "Videos",

    "music": HOME / "Music"

}


def score(kind, path):

    p = path.lower()

    s = 0

    if str(HOME).lower() in p:
        s += 1000

    if "desktop" in p:
        s += 900

    if "documents" in p:
        s += 800

    if "downloads" in p:
        s += 700

    if "pictures" in p:
        s += 600

    if "videos" in p:
        s += 500

    if "music" in p:
        s += 400

    if kind == "app":
        s += 300

    if "program files" in p:
        s += 200

    return s


def search(target):

    target = target.lower().strip()

    # ---------- Специални папки ----------

    if target in SPECIAL_FOLDERS:

        path = SPECIAL_FOLDERS[target]

        if path.exists():

            return (
                "folder",
                str(path)
            )

    results = []

    # ---------- Applications ----------

    for name, path in computer.apps.items():

        if name == target:

            results.append((
                "app",
                path,
                10000
            ))

        elif target in name:

            results.append((
                "app",
                path,
                score("app", path)
            ))

    # ---------- Folders ----------

    for name, path in computer.folders.items():

        if name == target:

            results.append((
                "folder",
                path,
                score("folder", path) + 5000
            ))

        elif target in name:

            results.append((
                "folder",
                path,
                score("folder", path)
            ))

    # ---------- Files ----------

    for name, path in computer.files.items():

        if name == target:

            results.append((
                "file",
                path,
                score("file", path) + 3000
            ))

        elif target in name:

            results.append((
                "file",
                path,
                score("file", path)
            ))

    if not results:
        return None

    results.sort(
        key=lambda x: x[2],
        reverse=True
    )

    kind, path, _ = results[0]

    return (
        kind,
        path
    )