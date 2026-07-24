import json
from pathlib import Path


FILE = Path(__file__).parent / "knowledge.json"


class Knowledge:

    def __init__(self):

        self.data = {}

        self.load()

    def load(self):

        if FILE.exists():

            try:

                with open(FILE, "r", encoding="utf-8") as f:

                    self.data = json.load(f)

            except Exception:

                self.data = {}

    def save(self):

        with open(FILE, "w", encoding="utf-8") as f:

            json.dump(
                self.data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def set(self, key, value):

        self.data[key] = value

        self.save()

    def get(self, key, default=None):

        return self.data.get(key, default)

    def delete(self, key):

        if key in self.data:

            del self.data[key]

            self.save()

    def all(self):

        return dict(self.data)

    def clear(self):

        self.data = {}

        self.save()


knowledge = Knowledge()
