from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, username):
        self.username = username
        self.projects = []