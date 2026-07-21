from developer.context import context
from developer.search import find_function
from developer.backup import backup
from developer.patcher import replace_text
from developer.runner import run_python
from developer.reviewer import has_error

from developer.dependency import dependency
from developer.symbols import symbols
from developer.workspace import workspace


class DeveloperAgent:

    def scan(self, root):

        context.scan(root)

        dependency.scan(root)

        symbols.scan(root)

        workspace.scan(root)

    def locate(self, function):

        return find_function(function)

    def patch(self, file, old, new):

        backup(file)

        replace_text(file, old, new)

    def test(self, file):

        return run_python(file)

    def stats(self):

        return {

            "python_files": workspace.count(),

            "indexed_files": len(context.files),

            "dependency_files": len(dependency.graph),

            "symbol_files": len(symbols.functions)

        }


developer = DeveloperAgent()