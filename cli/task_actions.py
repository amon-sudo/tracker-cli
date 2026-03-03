from rich import print

class TaskActions:

    # ---------- Add Task ----------
    def add_task(self, users, storage):
        username = input("Username: ")
        project_name = input("Project name: ")
        task_desc = input("Task description: ")

        for user in users:
            if user["username"] == username:

                for project in user.get("projects", []):

                    if project["name"] == project_name:

                        if "tasks" not in project:
                            project["tasks"] = []

                        project["tasks"].append({
                            "description": task_desc,
                            "completed": False
                        })

                        storage.save(users)

                        print("[green]Task added successfully[/green]")
                        return

                print("[red]Project not found[/red]")
                return

        print("[red]User not found[/red]")

    def complete_task(self, users, storage):
        username = input("Username: ")
        project_name = input("Project name: ")
        task_index = input("Task index (start from 0): ")

        try:
            task_index = int(task_index)
        except:
            print("[red]Invalid task index[/red]")
            return

        for user in users:
            if user["username"] == username:

                for project in user.get("projects", []):

                    if project["name"] == project_name:

                        if task_index >= len(project.get("tasks", [])):
                            print("[red]Task index out of range[/red]")
                            return

                        project["tasks"][task_index]["completed"] = True

                        storage.save(users)

                        print("[green]Task marked complete[/green]")
                        return

                print("[red]Project not found[/red]")
                return

        print("[red]User not found[/red]")