import os
from pathlib import Path

from computer.index import computer


USER = Path.home()

ROOTS = [

    USER / "Desktop",
    USER / "Documents",
    USER / "Downloads",
    USER / "Pictures",
    USER / "Videos",
    USER / "Music",

    Path("C:/Program Files"),
    Path("C:/Program Files (x86)"),

    Path(os.environ.get("LOCALAPPDATA", "")) / "Programs",

    Path(os.environ.get("PROGRAMDATA", "")) /
    "Microsoft/Windows/Start Menu/Programs",

    Path(os.environ.get("APPDATA", "")) /
    "Microsoft/Windows/Start Menu/Programs"

]


APP_EXTENSIONS = {

    ".exe",
    ".lnk",
    ".bat",
    ".cmd",
    ".msc"

}


def add_folder(folder):

    computer.add_folder(
        folder.name,
        str(folder)
    )

    computer.add_folder(
        folder.name.lower(),
        str(folder)
    )


def add_file(file):

    computer.add_file(
        file.name,
        str(file)
    )


def add_app(file):

    name = file.stem.lower().strip()

    if name not in computer.apps:

        computer.add_app(
            name,
            str(file)
        )


def scan():

    computer.clear()

    visited = set()

    for root in ROOTS:

        if not root.exists():
            continue

        try:
            add_folder(root)
        except Exception:
            pass

        for path in root.rglob("*"):

            try:

                path = path.resolve()

                key = str(path).lower()

                if key in visited:
                    continue

                visited.add(key)

                if path.is_dir():

                    add_folder(path)

                    continue

                add_file(path)

                if path.suffix.lower() in APP_EXTENSIONS:

                    add_app(path)

            except Exception:
                pass

    print(f"🟢 Applications : {len(computer.apps)}")
    print(f"📄 Files        : {len(computer.files)}")
    print(f"📁 Folders      : {len(computer.folders)}")

    return computer
