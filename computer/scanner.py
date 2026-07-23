import os
from pathlib import Path

from core.logger import logger
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
    "Microsoft/Windows/Start Menu/Programs",
]


APP_EXTENSIONS = {
    ".exe",
    ".lnk",
    ".bat",
    ".cmd",
    ".msc",
}


def add_folder(folder):

    computer.add_folder(
        folder.name,
        str(folder)
    )


def add_file(file):

    computer.add_file(
        file.name,
        str(file)
    )


def add_app(file):

    name = file.stem.lower().strip()

    computer.add_app(
        name,
        str(file)
    )


def scan():

    logger.info("🔍 Scanning computer...")

    computer.clear()

    visited = set()

    scanned = 0
    skipped = 0
    errors = 0

    for root in ROOTS:

        if not root.exists():
            continue

        try:
            add_folder(root)
        except Exception:
            errors += 1

        try:

            for path in root.rglob("*"):

                try:

                    path = path.resolve()

                    key = str(path).lower()

                    if key in visited:
                        skipped += 1
                        continue

                    visited.add(key)

                    scanned += 1

                    if path.is_dir():

                        add_folder(path)
                        continue

                    add_file(path)

                    if path.suffix.lower() in APP_EXTENSIONS:
                        add_app(path)

                except Exception:
                    errors += 1

        except Exception:
            errors += 1

    stats = computer.stats()

    logger.info(f"🟢 Applications : {stats['apps']}")
    logger.info(f"📄 Files        : {stats['files']}")
    logger.info(f"📁 Folders      : {stats['folders']}")
    logger.info(f"🔍 Scanned      : {scanned}")
    logger.info(f"⏭️ Skipped      : {skipped}")
    logger.info(f"⚠️ Errors       : {errors}")

    return computer
