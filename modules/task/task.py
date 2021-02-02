from datetime import datetime

from modules.task.note import Note
from modules.checker.checker import Checker


class Task(Note):

    def __init__(self, name="empty", text="there's no", to_date="18/09/25 01:55:19"):
        super().__init__(name, text)
        self.isDone = False
        self.fromDate = datetime.now()
        self.toDate = datetime.strptime(to_date, '%d/%m/%y %H:%M:%S')

    @staticmethod
    def add_task(tasks: list) -> None:
        try:
            print("Menu of make task")
            while True:
                name, text = input("name: ").strip(), input("text: ").strip()
                to_date = input("to date: ").strip()

                if Checker.data(datetime.strptime(to_date, '%d/%m/%y %H:%M:%S')):
                    print("the date must refer to the future")
                    continue
                elif Checker.unique(tasks, name):
                    print("name must be unique")
                    continue

                try:
                    return tasks.append(Task(name, text, to_date))
                except ValueError:
                    print("format of date is: %d/%m/%y %H:%M:%S, for example 18/09/21 01:55:19")
        except KeyboardInterrupt:
            return


    def done_status(self, status: bool):
        self.isDone = status

    def add_fromdate(self, data: str):
        self.fromDate = str

    def add_todate(self, data: str):
        self.toDate = data if self.toDate else self.toDate

    def change_todate(self, data: str):
        self.toDate = data if data else self.toDate

    def remind(self):
        print(self.text, "do task")

    def __repr__(self):
        return f'Task due {self.toDate} text of task: {self.text}'

    def __str__(self):
        return self.__repr__()
