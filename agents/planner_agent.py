from typing import Any, Dict, List


class PlannerAgent:
    """
    Planner Agent

    Разделя сложните задачи на последователни стъпки.
    Не изпълнява задачи, а само създава план.
    """

    name = "planner"

    def __init__(self):
        self.last_plan: List[Dict[str, Any]] = []

    @property
    def tools(self):
        return [
            "plan",
            "planner"
        ]

    def can_handle(self, action: Dict[str, Any]) -> bool:
        return action.get("agent", "").lower() == "planner"

    def execute(self, action: Dict[str, Any]) -> Dict[str, Any]:
        task = action.get("task") or action.get("message") or ""

        plan = self.create_plan(task)

        self.last_plan = plan

        return {
            "success": True,
            "task": task,
            "steps": plan,
            "total_steps": len(plan)
        }

    def create_plan(self, task: str) -> List[Dict[str, Any]]:
        """
        Създава базов план.
        По-късно ще се генерира от AI.
        """

        plan = [
            {
                "step": 1,
                "action": "analyze",
                "description": "Анализ на задачата",
                "status": "pending"
            },
            {
                "step": 2,
                "action": "select_agent",
                "description": "Избор на подходящ агент",
                "status": "pending"
            },
            {
                "step": 3,
                "action": "execute",
                "description": "Изпълнение на задачата",
                "status": "pending"
            },
            {
                "step": 4,
                "action": "validate",
                "description": "Проверка на резултата",
                "status": "pending"
            }
        ]

        return plan

    def get_last_plan(self):
        return self.last_plan

    def clear(self):
        self.last_plan = []

    def status(self):
        return {
            "plans_created": len(self.last_plan),
            "ready": True
        }
