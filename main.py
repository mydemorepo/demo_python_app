from flask import *
from services.mysqldb import mysqldb
from services.sqllitedb import sqllitedb
from services.jsonbuilder import jsonbuilder
from services.xmlbuilder import xmlbuilder
from services.csvbuilder import csvbuilder
import os

app = Flask(__name__)

# Sqlite використовується за замовчуванням. 
# Щоб використовувати MySql, інсталюйте сервер 
# MySql і відновіть базу даних 
# services/mysqldb/sampledatabase.sql із дампу.

# db = mysqldb.MysqlDb("localhost", "root", "root", "classicmodels",)
db = sqllitedb.SqlliteDb("sampledatabase.sqlite")
jb = jsonbuilder.JsonBuilder()
xb = xmlbuilder.XmlBuilder()
csvb = csvbuilder.CsvFileBuilder()


# При переході в корінь виводиться список таблиць.
@app.route('/')
def index():
    tables_list = db.get_tables()
    return render_template('main.html', tables_list=tables_list)


# При використанні GET запиту(клік на назву таблиці) виводиться вся таблиця.
# При використанні POST запиту (використання форми з можливістю вибору для 
# відображення певних колонок таблиці) відображаються лише ті колонки, 
# які були вибрані за допомогою чекбокс.
@app.route('/<table_name>', methods=['POST', 'GET'])
def tables(table_name):
    if request.method == 'GET':
        tables_list = db.get_tables()
        table = db.get_result(f"SELECT * FROM {table_name}")
        resp = make_response(render_template('tables.html',
                                             tables_list=tables_list,
                                             table=table,
                                             table_name=table_name))
        resp.set_cookie('QueryString', f"SELECT * FROM {table_name}")
        return resp
        
    elif request.method == 'POST': 
        data = request.form.to_dict(flat=True)
    
        colums_list = []
        for column in data:
            colums_list.append(column)
                 
        tables_list = db.get_tables()        
        table = db.get_result(f"SELECT {', '.join(colums_list)} FROM {table_name}")    
        resp = make_response(render_template('tables.html',
                                              tables_list=tables_list,
                                              table=table,
                                              table_name=table_name))
        resp.set_cookie('QueryString', f"SELECT {', '.join(colums_list)} FROM {table_name}")   
        return resp


# Повертається список таблиць у форматі JSON.
@app.route('/api/json')
def json_index(): 
    return jb.get_json(db.get_tables())


# При використанні GET запиту (наприклад get = requests.get('url/offices)) 
# повертається вся таблиця у форматі JSON.При використанні POST запиту 
# (наприклад post = requests.post(url/offices, data={'city': 'on', 'country': 'on'})) 
# повертаються у форматі JSON список таблиць та лише ті колонки, 
# які були вказані в словнику, який передається через параметр data.
@app.route('/api/json/<table_name>', methods=['POST', 'GET'])
def json_tables(table_name): 
    if request.method == 'GET':
        resp = make_response(jb.get_json(db.get_tables(),
                                         table_name,
                                         db.get_result(f"SELECT * FROM {table_name}")))
        resp.set_cookie('QueryString', f"SELECT * FROM {table_name}")
        return resp
    elif request.method == 'POST': 
        data = request.form.to_dict(flat=True)
    
        colums_list = []
        for column in data:
            colums_list.append(column)   
        resp = make_response(jb.get_json(db.get_tables(),
                                         table_name,
                                         db.get_result(f"SELECT {', '.join(colums_list)} FROM {table_name}")))
        resp.set_cookie('QueryString', f"SELECT {', '.join(colums_list)} FROM {table_name}")
        return resp


# Повертається список таблиць у форматі XML.
@app.route('/api/xml')
def xml_index(): 
    return xb.get_xml(db.get_tables())


# При використанні GET запиту (наприклад get = requests.get('url/offices)) 
# повертається вся таблиця у форматі XML.При використанні POST запиту 
# (наприклад post = requests.post(url/offices, data={'city': 'on', 'country': 'on'})) 
# повертаються у форматі XML список таблиць та лише ті колонки, 
# які були вказані в словнику, який передається через параметр data.
@app.route('/api/xml/<table_name>', methods=['POST', 'GET'])
def xml_tables(table_name): 
    if request.method == 'GET':
        resp = make_response(xb.get_xml(db.get_tables(),
                                        table_name,
                                        db.get_result(f"SELECT * FROM {table_name}")))
        resp.set_cookie('QueryString', f"SELECT * FROM {table_name}")
        return resp
    elif request.method == 'POST': 
        data = request.form.to_dict(flat=True)
    
        colums_list = []
        for column in data:
            colums_list.append(column)
        resp = make_response(xb.get_xml(db.get_tables(),
                                        table_name,
                                        db.get_result(f"SELECT {', '.join(colums_list)} FROM {table_name}")))
        resp.set_cookie('QueryString', f"SELECT {', '.join(colums_list)} FROM {table_name}")
        return resp


# При використанні GET запиту відправляютюся дані які 
# було отримано під час останнього запиту клієнта в 
# форматі CSV для збереження в файл на стороні клієнта.
@app.route('/download/<table_name>')
def download(table_name):
    QueryString = request.cookies.get('QueryString')
    csvb.get_csv(db.get_result(QueryString), table_name)
    path = os.path.join(app.root_path, 'downloads', f'{table_name}.csv')
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
