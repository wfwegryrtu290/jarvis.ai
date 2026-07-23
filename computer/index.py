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

                                                                        self.apps[name.lower().strip()] = path

                                                                            def add_file(self, name, path):

                                                                                    self.files[name.lower().strip()] = path

                                                                                        def add_folder(self, name, path):

                                                                                                self.folders[name.lower().strip()] = path

                                                                                                    def find(self, target):

                                                                                                            target = target.lower().strip()

                                                                                                                    # Точно съвпадение

                                                                                                                            if target in self.apps:
                                                                                                                                        return ("app", self.apps[target])

                                                                                                                                                if target in self.files:
                                                                                                                                                            return ("file", self.files[target])

                                                                                                                                                                    if target in self.folders:
                                                                                                                                                                                return ("folder", self.folders[target])

                                                                                                                                                                                        # Частично съвпадение

                                                                                                                                                                                                for collection, kind in (
                                                                                                                                                                                                            (self.apps, "app"),
                                                                                                                                                                                                                        (self.files, "file"),
                                                                                                                                                                                                                                    (self.folders, "folder"),
                                                                                                                                                                                                                                            ):

                                                                                                                                                                                                                                                        for name, path in collection.items():

                                                                                                                                                                                                                                                                        if target in name:
                                                                                                                                                                                                                                                                                            return (kind, path)

                                                                                                                                                                                                                                                                                                    return None


                                                                                                                                                                                                                                                                                                    computer = ComputerIndex()