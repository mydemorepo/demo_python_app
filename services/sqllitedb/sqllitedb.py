import sqlite3


class SqlliteDb():

    def __init__(self, db_name):
        self.db_name = db_name

    def get_result(self, query_string):
        db = sqlite3.connect(self.db_name)
        cursor = db.cursor()
        cursor.execute(query_string)
        data = cursor.fetchall()
        db.close()
        return data
    
    def get_tables(self):
        db = sqlite3.connect(self.db_name)
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type ='table'")
        data = cursor.fetchall()
        db.close()
        return data
    
    
