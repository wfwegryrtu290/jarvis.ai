class ComputerHistory:

    def __init__(self):

        self.clear()

    def clear(self):

        self.last_target = None
        self.last_file = None
        self.last_folder = None
        self.last_app = None
        self.last_window = None

    def remember(self, kind, path):

        self.last_target = path

        if kind == "file":
            self.last_file = path

        elif kind == "folder":
            self.last_folder = path

        elif kind == "app":
            self.last_app = path

        elif kind == "window":
            self.last_window = path


history = ComputerHistory()