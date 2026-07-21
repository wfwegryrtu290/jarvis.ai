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

    Path(os.environ.get("LOCALAPPDATA", "")) / "Programs"

]


APP_EXTENSIONS = {
    ".exe",
    ".lnk",
    ".bat",
    ".cmd"
}


def scan():

    computer.clear()

    for root in ROOTS:

        if not root.exists():
            continue

        # Индексираме самата папка
        computer.add_folder(
            root.name,
            str(root)
        )

        # Ако е Desktop/Documents и т.н. да може да се намира и по малки букви
        computer.add_folder(
            root.name.lower(),
            str(root)
        )

        for path in root.rglob("*"):

            try:

                if path.is_dir():

                    computer.add_folder(
                        path.name,
                        str(path)
                    )

                else:

                    computer.add_file(
                        path.name,
                        str(path)
                    )

                    if path.suffix.lower() in APP_EXTENSIONS:

                        computer.add_app(
                            path.stem,
                            str(path)
                        )

            except Exception:
                pass

    return computer