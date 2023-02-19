import pymysql


# Об'єкт класу MysqlDb використовується для 
# отримання результатів SQL запитів до бази данних.
class MysqlDb():

# При створенні об'єкта класу передаємо параметри для підключення до бази даних.
    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
    
# Отримання результатів SQL запиту до бази данних.
    def get_result(self, query_string):
    
    # Підключаємося до бази данних.   
        db = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             database=self.db_name,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        # Створюємо курсор, спеціальний об’єкт який робить запити і отримує їх результати.
        cursor = db.cursor()
        
        # Виконуємо SQL запит
        cursor.execute(query_string)
        
        # Отримуємо результат виконання запиту.
        data = cursor.fetchall()
       
        # Закриваємо з'єднання з базою даних.
        db.close()
        
        # Повертаємо результат у вигляді списку словників.
        return data

# Отримання списку таблиць бази данних.    
    def get_tables(self):
        # Підключаємося до бази данних.
        db = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             database=self.db_name,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        # Створюємо курсор, спеціальний об’єкт який робить запити і отримує їх результати.
        cursor = db.cursor() 
       
        # Виконуємо SQL запит, в результаті виконання 
        # якого отримуємо список таблиць в базі данних.
        cursor.execute("SHOW TABLES")
        
        # Отримуємо результат виконання запиту.
        data = cursor.fetchall()
       
        # Закриваємо з'єднання з базою даних.
        db.close()
        
        # Повертаємо результат у вигляді списку словників.
        return data

