class ComputerIndex:

    def __init__(self):

        self.apps = {}
        self.files = {}
        self.folders = {}

    def clear(self):

        self.apps.clear()
        self.files.clear()
        self.folders.clear()

    def add_app(self, name, path):

        if not name or not path:
            return

        self.apps[name.lower().strip()] = path

    def add_file(self, name, path):

        if not name or not path:
            return

        self.files[name.lower().strip()] = path

    def add_folder(self, name, path):

        if not name or not path:
            return

        self.folders[name.lower().strip()] = path

    def find(self, target):

        if not target:
            return None

        target = target.lower().strip()

        # Точно съвпадение

        if target in self.apps:
            return ("app", self.apps[target])

        if target in self.files:
            return ("file", self.files[target])

        if target in self.folders:
            return ("folder", self.folders[target])

        # Частично съвпадение

        collections = (
            (self.apps, "app"),
            (self.files, "file"),
            (self.folders, "folder"),
        )

        for collection, kind in collections:

            for name, path in collection.items():

                if target in name:
                    return (kind, path)

        return None

    def stats(self):

        return {
            "apps": len(self.apps),
            "files": len(self.files),
            "folders": len(self.folders),
            "total": (
                len(self.apps)
                + len(self.files)
                + len(self.folders)
            ),
        }

    def exists(self, target):

        return self.find(target) is not None


computer = ComputerIndex()                                                                                                                                                                                                                                                                                                    computer = ComputerIndex()
