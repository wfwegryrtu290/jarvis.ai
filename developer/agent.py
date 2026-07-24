from core.logger import logger

from developer.context import context
from developer.search import find_function
from developer.backup import backup
from developer.patcher import replace_text
from developer.runner import run_python
from developer.reviewer import has_error

from developer.dependency import dependency
from developer.symbols import symbols
from developer.workspace import workspace

from memory.manager import memory


class DeveloperAgent:

    def scan(self, root):

        logger.info(f"Scanning workspace: {root}")

        context.scan(root)
        dependency.scan(root)
        symbols.scan(root)
        workspace.scan(root)

        logger.info("Workspace indexed successfully.")

    def locate(self, function):

        logger.debug(f"Searching function: {function}")

        return find_function(function)

    def patch(self, file, old, new):

        logger.info(f"Patching file: {file}")

        backup(file)

        replace_text(file, old, new)

        logger.info("Patch completed.")

    def test(self, file):

        logger.info(f"Running: {file}")

        return run_python(file)

    def review(self, file):

        logger.info(f"Reviewing: {file}")

        return has_error(file)

    def stats(self):

        return {

            "python_files": workspace.count(),

            "indexed_files": len(context.files),

            "dependency_files": len(dependency.graph),

            "symbol_files": len(symbols.functions),

            "memory_messages": memory.count(),

            "agents": 0,

            "tools": 0

        }


developer = DeveloperAgent()
