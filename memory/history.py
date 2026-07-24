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

        return self.items[-1] if self.items else None

    def all(self):

        return list(self.items)

    def recent(self, limit=10):

        return list(self.items)[-limit:]

    def find(self, event):

        return [
            item
            for item in self.items
            if item["event"] == event
        ]

    def clear(self):

        self.items.clear()

    def count(self):

        return len(self.items)


history = History()
