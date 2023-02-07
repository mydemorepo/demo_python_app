from flask import *
from services.mysqldb import mysqldb
from services.sqllitedb import sqllitedb
app = Flask(__name__)

#  Sqlite is used by default.
#  To use MySql, install MySql 
#  Server and restore the 
#  sampledatabase.sql database 
#  from the dump.

#db = mysqldb.MysqlDb("localhost", "root", "root", "classicmodels",)

db = sqllitedb.SqlliteDb("sampledatabase.sqlite")


@app.route('/')
def index():
    tables_list = db.get_tables()
    return render_template('main.html', tables_list=tables_list)

@app.route('/<table_name>')
def tables(table_name):
    tables_list = db.get_tables()
    table = db.get_result(f"SELECT * FROM {table_name}")
    return render_template('tables.html', tables_list=tables_list, table = table)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
