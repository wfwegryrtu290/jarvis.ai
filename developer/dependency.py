import ast
import os

from core.logger import logger


class DependencyGraph:

    def __init__(self):

        self.graph = {}

    def clear(self):

        self.graph.clear()

    def scan(self, root):

        logger.info(f"Scanning dependencies: {root}")

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

                self.graph[full] = self.get_imports(full)

        logger.info(f"Dependency graph contains {len(self.graph)} files.")

    def get_imports(self, filename):

        imports = []

        try:

            with open(filename, "r", encoding="utf-8") as f:

                tree = ast.parse(f.read())

        except Exception as e:

            logger.debug(f"Cannot parse {filename}: {e}")

            return imports

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for module in node.names:
                    imports.append(module.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    imports.append(node.module)

        return sorted(set(imports))

    def dependencies(self, filename):

        return self.graph.get(filename, [])

    def reverse_dependencies(self, module):

        result = []

        for file, imports in self.graph.items():

            if any(module in imp for imp in imports):
                result.append(file)

        return result

    def has_dependency(self, filename, module):

        return module in self.graph.get(filename, [])

    def count(self):

        return len(self.graph)


dependency = DependencyGraph()
