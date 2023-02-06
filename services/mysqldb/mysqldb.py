import pymysql


class MysqlDb():

    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

    def get_result(self, query_string):
        db = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             database=self.db_name,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute(query_string)
        data = cursor.fetchall()
        db.close()
        return data

