from flask import *
from services.mysqldb import mysqldb
from services.sqllitedb import sqllitedb
app = Flask(__name__)


mysql_db = mysqldb.MysqlDb("localhost", "root", "root", "classicmodels",)
sqllite_db = sqllitedb.SqlliteDb()


@app.route('/')
def index():
    tables_list = mysql_db.get_result("SHOW TABLES")
    tables_listlite = sqllite_db.get_result("select * from employees")
    return render_template('main.html', tables_list=tables_list, tables_listlite = tables_listlite)

@app.route('/<table_name>')
def tables(table_name):
    tables_list = mysql_db.get_result("SHOW TABLES")
    table = mysql_db.get_result(f"SELECT * FROM {table_name}")
    return render_template('tables.html', tables_list=tables_list, table = table)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
