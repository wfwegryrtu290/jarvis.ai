from abc import ABC, abstractmethod


class BaseAgent(ABC):

    name = "base"
    description = ""
    tools = []

    def info(self):

        return {
            "name": self.name,
            "description": self.description,
            "tools": self.tools
        }

    @abstractmethod
    def can_handle(self, action):

        """
        Връща True ако агентът може
        да изпълни действието.
        """
        pass

    @abstractmethod
    def execute(self, action):

        """
        Изпълнява действието.
        """
        pass

    def __str__(self):

        return f"{self.name} ({len(self.tools)} tools)"

    def __repr__(self):

        return self.__str__()
