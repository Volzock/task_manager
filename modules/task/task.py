from datetime import datetime

from modules.task.note import Note
from modules.db.db import DataBase


class Task(Note):

    def __init__(self, text="there's no", fromDate="18/09/21 01:55:19", toDate="18/09/25 01:55:19"):
        super().__init__(text)
        self.isDone = False
        self.fromDate = datetime.strptime(fromDate, '%d/%m/%y %H:%M:%S')
        self.toDate = datetime.strptime(toDate, '%d/%m/%y %H:%M:%S')

    def data_push(self):
        DataBase.add_entry()

    def doneStatus(self, status: bool):
        self.isDone = status

    def addFromDate(self, data: str):
        self.fromDate = str

    def addToDate(self, data:str):
        self.toDate = data if self.toDate else self.toDate

    def changeToDate(self, data:str):
        self.toDate = data if data else self.toDate

    def remind(self):
        print(self.text, "do task")

    def __repr__(self):
        return f'Task due {self.toDate} text of task: {self.text}'

    def __str__(self):
        return self.__repr__()