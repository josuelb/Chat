from flask import Flask
import mysql.connector

app = Flask(__name__)

# Required
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chat_flask",
)


