import sqlite3


class SqlliteDb():

    def get_result(self, query_string):
        db = sqlite3.connect('data.sqlite')
        cursor = db.cursor()
        cursor.execute(query_string)
        data = cursor.fetchall()
        db.close()
        return data
