import pickle

from modules.task.task import Task
from modules.task_group.task_group import TaskGroup


class Application:

    def __init__(self):
        self.tasks = []
        self.groups = []
        self.history = []

    def start(self):
        try:
            while True:
                cmd = input("app: ").lower().strip().split()
                if cmd[0] == "make":
                    if cmd[1] == "task":
                        Task.add_task(self.tasks)
                    elif cmd[1] == "group":
                        TaskGroup.add_group(self.groups)
                elif cmd[0] == "list":
                    if cmd[1] == "tasks":
                        pass
                    elif cmd[1] == "groups":
                        pass
                elif cmd[0] == "edit":
                    pass
                elif cmd[0] == "view":
                    pass
                elif cmd[0] == "remove":
                    if cmd[1] == "task":
                        self.remove_task(cmd[2])
                    elif cmd[1] == "group":
                        self.remove_group(cmd[2])
                elif cmd[0] == "done":
                    pass
                elif cmd[0] == "add":
                    pass
                elif cmd[0] == "help":
                    self.print_help()
        except KeyboardInterrupt:
            print("Bye bye")

    def remove_task(self, name):
        pass

    def remove_group(self, name):
        pass

    def print_help(self):
        with open("data/help.txt") as help_txt:
            for string in help_txt:
                print(string)
        print()

    def __del__(self):
        pass
