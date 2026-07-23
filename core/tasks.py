class TaskQueue:

    def __init__(self):

        self.tasks = []

    def add(self, task):

        self.tasks.append(task)

    def next(self):

        if not self.tasks:
            return None

        return self.tasks.pop(0)

    def peek(self):

        if not self.tasks:
            return None

        return self.tasks[0]

    def clear(self):

        self.tasks.clear()

    def size(self):

        return len(self.tasks)

    def empty(self):

        return len(self.tasks) == 0

    def __len__(self):

        return len(self.tasks)

    def __iter__(self):

        return iter(self.tasks)


queue = TaskQueue()
