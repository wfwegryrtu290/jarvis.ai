from ai.planner import create_plan
from core.logger import logger


class LoopPlanner:

    def create(self, message):

        logger.info("Loop Planner")

        plan = create_plan(message)

        if not isinstance(plan, dict):

            return None

        if "actions" not in plan:

            plan["actions"] = []

        if "thought" not in plan:

            plan["thought"] = ""

        if "answer" not in plan:

            plan["answer"] = ""

        return plan

    def has_actions(self, plan):

        if not plan:

            return False

        return len(plan.get("actions", [])) > 0

    def next_action(self, plan):

        actions = plan.get("actions", [])

        if not actions:

            return None

        return actions.pop(0)


planner = LoopPlanner()
