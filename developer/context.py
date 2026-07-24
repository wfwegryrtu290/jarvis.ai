import ast
import os

from core.logger import logger


class ProjectContext:

    def __init__(self):

        self.files = []
        self.imports = {}
        self.functions = {}
        self.classes = {}

    def clear(self):

        self.files.clear()
        self.imports.clear()
        self.functions.clear()
        self.classes.clear()

    def scan(self, root):

        logger.info(f"Scanning project: {root}")

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

                if not file.endswith(".py"):
                    continue

                full = os.path.join(path, file)

                self.files.append(full)

                self.analyze(full)

        logger.info(f"Indexed {len(self.files)} Python files.")

    def analyze(self, filename):

        try:

            with open(filename, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)

        except Exception as e:

            logger.debug(f"Cannot parse {filename}: {e}")

            return

        imports = []
        functions = []
        classes = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for module in node.names:
                    imports.append(module.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    imports.append(node.module)

            elif isinstance(node, ast.FunctionDef):

                functions.append(node.name)

            elif isinstance(node, ast.AsyncFunctionDef):

                functions.append(node.name)

            elif isinstance(node, ast.ClassDef):

                classes.append(node.name)

        self.imports[filename] = imports
        self.functions[filename] = functions
        self.classes[filename] = classes

    def file_count(self):

        return len(self.files)

    def has_file(self, filename):

        return filename in self.files

    def get_functions(self, filename):

        return self.functions.get(filename, [])

    def get_imports(self, filename):

        return self.imports.get(filename, [])

    def get_classes(self, filename):

        return self.classes.get(filename, [])


context = ProjectContext()
