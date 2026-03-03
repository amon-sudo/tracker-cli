from rich import print

class ProjectActions:

    def list_users(self, users):
        print("\n[bold cyan]Users List[/bold cyan]")

        for user in users:
            print(user["username"])

    def add_project(self, users, storage):
        username = input("User username: ")
        project_name = input("Project name: ")

        for user in users:
            if user["username"] == username:

                if "projects" not in user:
                    user["projects"] = []

                user["projects"].append({
                    "name": project_name,
                    "tasks": []
                })

                storage.save(users)
                print("[green]Project added[/green]")
                return

        print("[red]User not found[/red]")