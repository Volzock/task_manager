import sqlite3

"""
 curr.fetchone() - получение только одной записи
"""


class DataBase:

    def __init__(self):
        self.conn = sqlite3.connect(f'data/db/data.db')
        self.cur = self.conn.cursor()

        with open("modules/db/init.sql") as cmds:
            self.cur.executescript(cmds.read())

    def add_entry(self, table_name, data):
        query_data = data.__str__().replace("{", "(").replace("}", ")")
        query = f"INSERT INTO {table_name} VALUES {query_data}"
        self.conn.commit()

    def __del__(self):
        self.conn.close()
