from rich import print
from storage.file_storage import FileStorage
from models.user import User
from cli.project_actions import ProjectActions
from cli.task_actions import TaskActions

class Menu:
    def __init__(self):
        self.storage = FileStorage("users.json")
        self.users = self.storage.load()
        self.current_user = None

        self.project_actions = ProjectActions()
        self.task_actions = TaskActions()

    # ---------- Main Menu ----------
    def start(self):
        while True:
            print("\n[bold cyan]PROJECT TRACKER SYSTEM[/bold cyan]")
            print("1. Register User")
            print("2. Login User")
            print("3. Exit")
            print("4. List Users")
            print("5. Add Project")
            print("6. Add Task")
            print("7. Complete Task")

            choice = input("Choice: ")

            if choice == "1":
                self.register_user()

            elif choice == "2":
                self.login_user()

            elif choice == "3":
                print("Goodbye!")
                break

            elif choice == "4":
                self.project_actions.list_users(self.users)

            elif choice == "5":
                self.project_actions.add_project(self.users, self.storage)

            elif choice == "6":
                self.task_actions.add_task(self.users, self.storage)

            elif choice == "7":
                self.task_actions.complete_task(self.users, self.storage)

    # ---------- Register User ----------
    def register_user(self):
        username = input("Enter username: ")

        for user in self.users:
            if user["username"] == username:
                print("[red]User already exists[/red]")
                return

        new_user = User(username)

        self.users.append(new_user.to_dict())
        self.storage.save(self.users)

        print("[green]User registered successfully[/green]")

    # ---------- Login User ----------
    def login_user(self):
        username = input("Username: ")

        for user in self.users:
            if user["username"] == username:
                self.current_user = user
                print("[green]Login successful[/green]")
                return

        print("[red]User not found[/red]")