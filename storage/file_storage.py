import json
import os

class FileStorage:
    def __init__(self, filename):
        os.makedirs("data", exist_ok=True)
        self.filename = os.path.join("data", filename)

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)