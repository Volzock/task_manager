from classes.task.task import Task


class TaskGroup:

    def __init__(self, group_name="", ):
        self.tasks = []
        self.group_name = ""

    def addGroupName(self, name: str):
        self.group_name = name

    def changeGroupName(self, name: str):
        self.group_name = name if name else self.group_name

    def removeGroupName(self):
        self.group_name = ""

    def addTask(self, task: Task):
        self.tasks.append(task)

    def removeTask(self, id: int):
        del self.tasks[id]

    def __repr__(self):
        tasks_str = ",".join(task for task in self.tasks)
        return f"{self.group_name}, tasks: {tasks_str}"