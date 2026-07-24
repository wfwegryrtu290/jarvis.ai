from memory.database import database


class MemoryManager:

    def save(self, user, assistant):

        database.save(user, assistant)

    def recent(self, limit=10):

        return database.recent(limit)

    def count(self):

        return database.count()

    def clear(self):

        database.clear()

    def context(self, limit=10):

        messages = self.recent(limit)

        if not messages:
            return ""

        lines = []

        for row in messages:

            try:
                user = row["user"]
                assistant = row["assistant"]
            except Exception:
                user, assistant = row

            lines.append(f"User: {user}")
            lines.append(f"Assistant: {assistant}")

        return "\n".join(lines)


memory = MemoryManager()
