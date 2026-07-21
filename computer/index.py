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

        self.apps[name.lower()] = path

    def add_file(self, name, path):

        self.files[name.lower()] = path

    def add_folder(self, name, path):

        self.folders[name.lower()] = path

    def find(self, target):

        target = target.lower().strip()

        if target in self.apps:
            return ("app", self.apps[target])

        if target in self.files:
            return ("file", self.files[target])

        if target in self.folders:
            return ("folder", self.folders[target])

        for name, path in self.apps.items():

            if target in name:
                return ("app", path)

        for name, path in self.files.items():

            if target in name:
                return ("file", path)

        for name, path in self.folders.items():

            if target in name:
                return ("folder", path)

        return None


computer = ComputerIndex()