from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseAgent(ABC):
    """
    Базов клас за всички агенти.
    """

    name = "base"
    description = "Base Agent"
    tools: List[str] = []

    @abstractmethod
    def can_handle(self, task: Dict[str, Any]) -> bool:
        """
        Проверява дали агентът може да изпълни задачата.
        """
        pass

    @abstractmethod
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Изпълнява задачата.
        """
        pass

    def status(self) -> Dict[str, Any]:
        """
        Информация за Dashboard.
        """
        return {
            "name": self.name,
            "description": self.description,
            "tools": self.tools,
            "ready": True,
        }

    def health(self) -> Dict[str, Any]:
        """
        Health Monitor.
        """
        return {
            "agent": self.name,
            "healthy": True,
        }
