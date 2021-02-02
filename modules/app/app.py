from modules.task.task import Task
from modules.task_group.task_group import TaskGroup


class Application:

    def __init__(self):
        self.tasks = []
        self.groups = []

    def start(self):
        while True:
            cmd = input("app> ").lower().strip().split()
            if cmd[0] == "make":
                if cmd[1] == "task":
                    Task.add_task(self.tasks)
                elif cmd[1] == "group":
                    TaskGroup.add_group(self.groups)
            elif cmd[0] == "list":
                pass
            elif cmd[0] == "edit":
                pass
            elif cmd[0] == "view":
                pass
            elif cmd[0] == "remind":
                pass
            elif cmd[0] == "remove":
                pass
            elif cmd[0] == "done":
                pass
            elif cmd[0] == "add":
                pass
            elif cmd[1] == "group":
                pass
            elif cmd[1] == "task":
                pass
            elif cmd[1] == "tasks":
                pass
            elif cmd[1] == "groups":
                pass
            elif cmd[1] == "help":
                pass

    def __del__(self):
        pass
