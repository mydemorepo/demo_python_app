from flask import *
from services.mysqldb import mysqldb
app = Flask(__name__)


@app.route('/')
def index():
    mysql_db = mysqldb.MysqlDb("localhost", "root", "root", "classicmodels",)
    tables_list = mysql_db.get_result("SHOW TABLES")
    return render_template('main.html', tables_list=tables_list)

@app.route('/<table_name>')
def tables(table_name):
    mysql_db = mysqldb.MysqlDb("localhost", "root", "root", "classicmodels",)
    tables_list = mysql_db.get_result("SHOW TABLES")
    table = mysql_db.get_result(f"SELECT * FROM {table_name}")
    return render_template('tables.html', tables_list=tables_list, table = table)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
