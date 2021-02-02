from datetime import datetime


class Checker:

    @staticmethod
    def data(time: datetime) -> bool:
        return time < datetime.now()

    @staticmethod
    def unique(items: list, item) -> bool:
        return item in [i.name for i in items]