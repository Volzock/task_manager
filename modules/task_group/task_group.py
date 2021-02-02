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

    def addGroupName(self, name: str):
        self.name = name

    def changeGroupName(self, name: str):
        self.name = name if name else self.name

    def removeGroupName(self):
        self.name = ""

    def addTask(self, task: Task):
        self.tasks.append(task)

    def removeTask(self, id: int):
        del self.tasks[id]

    def __repr__(self):
        tasks_str = ",".join(task for task in self.tasks)
        return f"{self.name}, tasks: {tasks_str}"