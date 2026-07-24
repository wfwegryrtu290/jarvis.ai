from collections import deque


class History:

    def __init__(self, max_items=100):

        self.max_items = max_items
        self.items = deque(maxlen=max_items)

    def add(self, event, data=None):

        self.items.append({
            "event": event,
            "data": data
        })

    def last(self):

        if not self.items:
            return None

        return self.items[-1]

    def all(self):

        return list(self.items)

    def clear(self):

        self.items.clear()

    def count(self):

        return len(self.items)


history = History()
