import ast
import os


class DependencyGraph:

    def __init__(self):

        self.graph = {}

    def scan(self, root):

        self.graph.clear()

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

                self.graph[full] = self.get_imports(full)

    def get_imports(self, filename):

        imports = []

        try:

            with open(filename, "r", encoding="utf-8") as f:

                tree = ast.parse(f.read())

        except Exception:

            return imports

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for n in node.names:

                    imports.append(n.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:

                    imports.append(node.module)

        return imports

    def dependencies(self, filename):

        return self.graph.get(filename, [])

    def reverse_dependencies(self, module):

        result = []

        for file, imports in self.graph.items():

            for imp in imports:

                if module in imp:

                    result.append(file)

        return result


dependency = DependencyGraph()