class BaseAgent:

    name = "base"

    def can_handle(self, task):

        return False

    def execute(self, task):

        raise NotImplementedError