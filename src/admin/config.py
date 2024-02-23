from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Required
app.config["MYSQL_USER"] = "root"
app.config["MSQL_PASSWORD"] = ""
