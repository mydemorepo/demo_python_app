import sqlite3


class SqlliteDb():

    def __init__(self, db_name):
        self.db_name = db_name

    def get_result(self, query_string):
        db = sqlite3.connect(self.db_name)
        cursor = db.cursor()
        
        cursor.execute(query_string)
        data = cursor.fetchall()
        
        cursor.execute(f'PRAGMA table_info({query_string.split()[-1]})')
        column_info = cursor.fetchall()
        db.close()
        
        table_content = []
        for line in data:
            line_dict = {}
            for cell_content, colum_name in zip(line, column_info):
                line_dict[colum_name[1]] = cell_content
            table_content.append(line_dict)
               
        db.close()
        
        return table_content
    
    def get_tables(self):
        db = sqlite3.connect(self.db_name)
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type ='table'")
        table_names = cursor.fetchall()
        db.close()
        
        tables_list = []
        for table in table_names:          
            tables_list.append({'Table_name':table[0]})
       
        return tables_list
    