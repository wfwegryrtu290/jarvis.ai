from tools.registry import get_tools

from core.logger import logger

from memory.manager import memory
from history.history import history


class Executor:

    def __init__(self):

        self.tools = get_tools()

    def execute(self, plan):

        actions = plan.get("actions", [])

        results = []

        for action in actions:

            tool_name = action.get("tool")
            args = action.get("args", {})

            tool = self.tools.get(tool_name)

            if tool is None:

                results.append({
                    "success": False,
                    "tool": tool_name,
                    "error": "Unknown tool."
                })

                continue

            try:

                logger.info(f"Tool: {tool_name}")
                logger.debug(args)

                result = tool["function"](**args)

                history.add(
                    tool_name,
                    result
                )

                memory.add_action(
                    tool_name,
                    args,
                    result
                )

                results.append(result)

            except Exception as e:

                logger.exception(e)

                results.append({
                    "success": False,
                    "tool": tool_name,
                    "error": str(e)
                })

        return {
            "success": True,
            "results": results
        }


executor = Executor()
