import os
import ast


class ProjectContext:

    def __init__(self):

        self.files = []
        self.imports = {}
        self.functions = {}

    def scan(self, root):

        self.files.clear()
        self.imports.clear()
        self.functions.clear()

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

                full = os.path.join(path, file)

                self.files.append(full)

                self.analyze(full)

    def analyze(self, filename):

        try:

            with open(filename, "r", encoding="utf-8") as f:

                source = f.read()

            tree = ast.parse(source)

        except Exception:

            return

        imports = []
        funcs = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for n in node.names:
                    imports.append(n.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    imports.append(node.module)

            elif isinstance(node, ast.FunctionDef):

                funcs.append(node.name)

        self.imports[filename] = imports
        self.functions[filename] = funcs


context = ProjectContext()