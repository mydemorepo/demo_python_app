from flask import *
from services.mysqldb import mysqldb
app = Flask(__name__)

@app.route('/')
def index():
    mysql_db = mysqldb.MysqlDb("localhost", "root", "root", "classicmodels",)
    data = mysql_db.get_result("SHOW TABLES")
    return render_template('main.html', data = data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
