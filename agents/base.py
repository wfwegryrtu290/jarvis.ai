class BaseAgent:

    name = "base"

    tools = []

    def can_handle(self, action):
        return False

    def execute(self, action):
        raise NotImplementedError