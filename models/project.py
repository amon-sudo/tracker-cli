from .base_model import BaseModel

class Project(BaseModel):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.tasks = []