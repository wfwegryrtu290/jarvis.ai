import os

from core.logger import logger


class Workspace:

    def __init__(self):

        self.files = []

    def clear(self):

        self.files.clear()

    def scan(self, root):

        logger.info(f"Scanning workspace: {root}")

        self.clear()

        for path, dirs, files in os.walk(root):

            dirs[:] = [
                d for d in dirs
                if d not in (
                    "__pycache__",
                    ".git",
                    ".venv",
                    "venv",
                    ".idea",
                    ".vscode",
                )
            ]

            for file in files:

                if file.endswith(".py"):

                    self.files.append(
                        os.path.join(path, file)
                    )

        logger.info(f"Found {len(self.files)} Python files.")

    def count(self):

        return len(self.files)

    def list(self):

        return list(self.files)

    def exists(self, filename):

        return filename in self.files

    def find(self, name):

        name = name.lower()

        for file in self.files:

            if os.path.basename(file).lower() == name:
                return file

        return None


workspace = Workspace()
