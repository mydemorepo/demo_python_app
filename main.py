from flask import *
from services.mysqldb import mysqldb
from services.sqllitedb import sqllitedb
from services.jsonbuilder import jsonbuilder
from services.xmlbuilder import xmlbuilder
from services.csvbuilder import csvbuilder
import os

app = Flask(__name__)

#  Sqlite is used by default.
#  To use MySql, install MySql 
#  Server and restore the 
#  services/mysqldb/sampledatabase.sql database 
#  from the dump.

# db = mysqldb.MysqlDb("localhost", "root", "root", "classicmodels",)
db = sqllitedb.SqlliteDb("sampledatabase.sqlite")
jb = jsonbuilder.JsonBuilder()
xb = xmlbuilder.XmlBuilder()
csvb = csvbuilder.CsvFileBuilder()


@app.route('/')
def index():
    tables_list = db.get_tables()
    return render_template('main.html', tables_list=tables_list)


@app.route('/<table_name>')
def tables(table_name):
    tables_list = db.get_tables()
    table = db.get_result(f"SELECT * FROM {table_name}")
    return render_template('tables.html', tables_list=tables_list, table=table, table_name = table_name)


@app.route('/api/json')
def json_index(): 
    return jb.get_json(db.get_tables())


@app.route('/api/json/<table_name>')
def json_tables(table_name): 
    return jb.get_json(db.get_tables(), table_name, db.get_result(f"SELECT * FROM {table_name}"))


@app.route('/api/xml')
def xml_index(): 
    return xb.get_xml(db.get_tables())


@app.route('/api/xml/<table_name>')
def xml_tables(table_name): 
    return xb.get_xml(db.get_tables(), table_name, db.get_result(f"SELECT * FROM {table_name}"))


@app.route('/download/<table_name>')
def download(table_name):
    csvb.get_csv(db.get_result(f"SELECT * FROM {table_name}"), table_name)
    path = os.path.join(app.root_path, 'downloads', f'{table_name}.csv')
    return send_file(path, as_attachment=True)

@app.route('/sendemail/<table_name>')
def send_email(table_name):
    return f'<a href="/{table_name}">Email {table_name} done! Go home.</a>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
