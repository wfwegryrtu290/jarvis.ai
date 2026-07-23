class State:

    def __init__(self):

        self.values = {}

    def set(self, key, value):

        self.values[key] = value

    def get(self, key, default=None):

        return self.values.get(key, default)

    def has(self, key):

        return key in self.values

    def remove(self, key):

        if key in self.values:
            del self.values[key]

    def clear(self):

        self.values.clear()

    def update(self, values):

        if isinstance(values, dict):
            self.values.update(values)

    def all(self):

        return self.values.copy()

    def __contains__(self, key):

        return key in self.values

    def __len__(self):

        return len(self.values)

    def __repr__(self):

        return f"State({self.values})"


state = State()
