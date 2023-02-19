import sqlite3


# Об'єкт класу MysqlDb використовується для 
# отримання результатів SQL запитів до бази данних.
class SqlliteDb():

# При створенні об'єкта класу передаємо параметри для підключення до бази даних.
    def __init__(self, db_name):
        self.db_name = db_name

# Отримання результатів SQL запиту до бази данних.
    def get_result(self, query_string):
       
        # Підключаємося до бази данних.
        db = sqlite3.connect(self.db_name)
       
        # Створюємо курсор, спеціальний об’єкт який робить запити і отримує їх результати.
        cursor = db.cursor()
        
        # Виконуємо SQL запит
        cursor.execute(query_string)
        
        # Отримуємо результат виконання запиту.
        data = cursor.fetchall()
        
# Оскільки cursor.fetchall() повертає результат 
# у вигляді списку кортежів, перетворимо їх у список словників, 
# де ключами будуть назви колонок а значеннями дані комірки.        
        
        # Створення списку кортежів, який буде містити інформіцію про колонки.
        column_info = []
        
        # Якщо в SQL запиті вибираємо всі колонки, то додаємо 
        # інформацію про них до списку який, міститить інформіцію про колонки.
        if  query_string.find('*') != -1:
            cursor.execute(f'PRAGMA table_info({query_string.split()[-1]})')
            column_info = cursor.fetchall()
            db.close()
        
        # Якщо в SQL запиті перелічені окремі колонки, 
        # то отримаємо їх імена з SQL запиту, та додамо інформацію
        # про нихдо списку який, міститить інформіцію про колонки.  
        else:
            for column_name in query_string.split()[1:-2]:
                if column_name.find(',') != -1:
                    column_info.append(('column_name', column_name[0:-1]))
                else:
                    column_info.append(('column_name', column_name))
                    
        # Створення списку словників, якиї містить у собі результат виконання SQL запиту.                          
        table_content = []
        for line in data:
            line_dict = {}
            for cell_content, colum_name in zip(line, column_info):
                line_dict[colum_name[1]] = cell_content
            table_content.append(line_dict)
         
        # Закриваємо з'єднання з базою даних.       
        db.close()
        
        # Повертаємо результат у вигляді списку словників.
        return table_content

# Отримання списку таблиць бази данних.    
    def get_tables(self):
        
        # Підключаємося до бази данних.
        db = sqlite3.connect(self.db_name)
       
        # Створюємо курсор, спеціальний об’єкт який робить запити і отримує їх результати.
        cursor = db.cursor()
        
        # Виконуємо SQL запит, в результаті виконання 
        # якого отримуємо інформацію про таблиці бази 
        # даних у вигляді списку кортежів.
        cursor.execute("SELECT name FROM sqlite_master WHERE type ='table'")
        
        # Отримуємо результат виконання запиту.
        table_names = cursor.fetchall()
        
        # Закриваємо з'єднання з базою даних.
        db.close()
        
# Оскільки cursor.fetchall() повертає результат 
# у вигляді списку кортежів, перетворимо їх у список словників, 
# де ключами буде рядок 'Table_name' а значеннями імена таблиць.
        tables_list = []
        for table in table_names: 
            tables_list.append({'Table_name':table[0]})
        
        # Повертаємо результат у вигляді списку словників.
        return tables_list
    
