from memory.database import database


class MemoryManager:

    def save(self, user, assistant):
        database.save(user, assistant)

    def recent(self, limit=10):
        return database.recent(limit)

    def clear(self):
        database.clear()

    def count(self):
        return database.count()


memory = MemoryManager()
