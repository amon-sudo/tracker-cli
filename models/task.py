from .base_model import BaseModel

class Task(BaseModel):
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed