import sqlite3


class Database:

    def __init__(self, db_path="test_data/test.db"):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def execute_query(self, query, parameters=None):
        if self.connection is None:
            self.connect()

        cursor = self.connection.cursor()

        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)

        return cursor.fetchall()

    def execute_update(self, query, parameters=None):
        if self.connection is None:
            self.connect()

        cursor = self.connection.cursor()

        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)

        self.connection.commit()

        return cursor.rowcount

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None