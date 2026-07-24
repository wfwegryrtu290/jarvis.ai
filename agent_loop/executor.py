from agents.manager import manager
from core.logger import logger


class LoopExecutor:

    def execute(self, action):

        if action is None:

            return {
                "success": False,
                "error": "Empty action."
            }

        logger.info(
            f"Executing: {action.get('tool')}"
        )

        try:

            result = manager.execute(action)

            if result is None:

                return {
                    "success": False,
                    "error": "Agent returned None."
                }

            return result

        except Exception as e:

            logger.exception(e)

            return {
                "success": False,
                "error": str(e)
            }

    def execute_plan(self, plan):

        results = []

        for action in plan.get("actions", []):

            result = self.execute(action)

            results.append(result)

            if not result.get("success", False):

                break

        return results


executor = LoopExecutor()
