import os


class Workspace:

    def __init__(self):

        self.files = []

    def scan(self, root):

        self.files.clear()

        for path, dirs, files in os.walk(root):

            dirs[:] = [
                d for d in dirs
                if d not in (
                    "__pycache__",
                    ".git",
                    ".venv",
                    "venv"
                )
            ]

            for file in files:

                if file.endswith(".py"):

                    self.files.append(
                        os.path.join(path, file)
                    )

    def count(self):

        return len(self.files)

    def list(self):

        return self.files


workspace = Workspace()