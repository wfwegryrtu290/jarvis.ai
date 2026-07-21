import os
from pathlib import Path


class ApplicationScanner:

    def __init__(self):

        self.apps = {}

    def scan(self):

        self.apps.clear()

        roots = [

            Path("C:/Program Files"),

            Path("C:/Program Files (x86)"),

            Path(os.environ.get("LOCALAPPDATA", "")) / "Programs",

            Path(os.environ.get("PROGRAMDATA", "")) /
            "Microsoft/Windows/Start Menu/Programs"
        ]

        for root in roots:

            if not root.exists():
                continue

            for file in root.rglob("*"):

                if file.suffix.lower() not in [".exe", ".lnk"]:
                    continue

                name = file.stem.lower()

                self.apps[name] = str(file)

        print(f"Indexed {len(self.apps)} applications.")

        return self.apps

    def find(self, name):

        name = name.lower().strip()

        # точно съвпадение
        if name in self.apps:
            return self.apps[name]

        # частично съвпадение
        for app_name, path in self.apps.items():

            if name in app_name:
                return path

        return None

    def all(self):

        return self.apps


scanner = ApplicationScanner()