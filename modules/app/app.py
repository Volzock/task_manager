import pickle

from modules.task.task import Task
from modules.task_group.task_group import TaskGroup


class Application:

    def __init__(self):
        self.groups = []

    def start(self):
        try:
            while True:
                cmd = input("app: ").lower().strip().split()
                if cmd[0] == "make":
                    TaskGroup.add_group(self.groups)
                elif cmd[0] == "edit":
                    if cmd[1] == "group":
                        pass
                    elif cmd[1] == "task":
                        pass
                elif cmd[0] == "view":
                    if cmd[1] == "groups":
                        self.print_groups()
                    elif cmd[1] == "group" and len(cmd) == 3:
                        print(self.groups[self.group_index_by_name(cmd[2])])
                    elif cmd[1] == "task" and len(cmd) == 4:
                        # view task in [3]
                        pass
                elif cmd[0] == "remove" and len(cmd) == 3:
                    if cmd[1] == "group":
                        self.remove_group(cmd[2])
                    elif cmd[1] == "task":
                        pass
                elif cmd[0] == "done":
                    pass
                elif cmd[0] == "add":
                    pass
                elif cmd[0] == "help":
                    self.print_help()
                else:
                    print("Error command")
                    print()
        except KeyboardInterrupt:
            print("Bye bye")

    def remove_group(self, name):
        del self.groups[self.group_index_by_name(name)]

    def print_help(self):
        with open("data/help.txt") as help_txt:
            for string in help_txt:
                print(string)
        print()

    def group_index_by_name(self, name):
        try:
            return [group.name for group in self.groups].index(name)
        except ValueError:
            print(f"There is no {name} in groups")

    def print_groups(self):
        for group in self.groups:
            print(group.name)
        print()

    def __del__(self):
        pass
