import ast
import os

from core.logger import logger


class SymbolTable:

    def __init__(self):

        self.functions = {}
        self.classes = {}

    def clear(self):

        self.functions.clear()
        self.classes.clear()

    def scan(self, root):

        logger.info(f"Scanning symbols: {root}")

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

                self.parse(
                    os.path.join(path, file)
                )

        logger.info(
            f"Indexed {len(self.functions)} Python files."
        )

    def parse(self, filename):

        try:

            with open(filename, "r", encoding="utf-8") as f:

                tree = ast.parse(f.read())

        except Exception as e:

            logger.debug(f"Cannot parse {filename}: {e}")

            return

        functions = []
        classes = []

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                functions.append(node.name)

            elif isinstance(node, ast.AsyncFunctionDef):

                functions.append(node.name)

            elif isinstance(node, ast.ClassDef):

                classes.append(node.name)

        self.functions[filename] = sorted(set(functions))
        self.classes[filename] = sorted(set(classes))

    def find_function(self, name):

        result = []

        for file, functions in self.functions.items():

            if name in functions:

                result.append(file)

        return result

    def find_class(self, name):

        result = []

        for file, classes in self.classes.items():

            if name in classes:

                result.append(file)

        return result

    def function_count(self):

        return sum(
            len(v)
            for v in self.functions.values()
        )

    def class_count(self):

        return sum(
            len(v)
            for v in self.classes.values()
        )


symbols = SymbolTable()
