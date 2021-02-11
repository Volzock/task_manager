from modules.task.task import Task
from modules.checker.checker import Checker


class TaskGroup:

    def __init__(self, name="", ):
        self.tasks = []
        self.name = name

    @staticmethod
    def add_group(groups: list):
        try:
            print("Menu of make group")
            while True:
                name = input("name: ")
                if Checker.unique(groups, name):
                    print("name must be unique")
                    continue
                else:
                    return groups.append(TaskGroup(name))
        except KeyboardInterrupt:
            return

    def change_group_name(self, name: str):
        self.name = name if name else self.name

    def add_task(self):
        self.tasks.append(Task.add_task(self.tasks))

    def remove_task(self, name: str):
        del self.tasks[[task.name for task in self.tasks].index(name)]

    def __repr__(self):
        tasks_str = "\n   ".join(task.name for task in self.tasks)
        return f"{self.name}\n tasks: {tasks_str}"