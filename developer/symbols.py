import ast
import os


class SymbolTable:

    def __init__(self):

        self.functions = {}
        self.classes = {}

    def scan(self, root):

        self.functions.clear()
        self.classes.clear()

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

                if not file.endswith(".py"):

                    continue

                self.parse(os.path.join(path, file))

    def parse(self, filename):

        try:

            with open(filename, "r", encoding="utf-8") as f:

                tree = ast.parse(f.read())

        except Exception:

            return

        funcs = []
        classes = []

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                funcs.append(node.name)

            elif isinstance(node, ast.ClassDef):

                classes.append(node.name)

        self.functions[filename] = funcs
        self.classes[filename] = classes

    def find_function(self, name):

        result = []

        for file, funcs in self.functions.items():

            if name in funcs:

                result.append(file)

        return result

    def find_class(self, name):

        result = []

        for file, classes in self.classes.items():

            if name in classes:

                result.append(file)

        return result


symbols = SymbolTable()