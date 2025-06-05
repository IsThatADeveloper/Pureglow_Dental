from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc5434fee1ccf15749238b4b14878f1d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from main import routes

def init_db():
    conn = sqlite3.connect('instance/appointments.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments
                      (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, email TEXT, service TEXT, number TEXT, date TEXT, time TEXT)''')
    conn.commit()
    conn.close()

init_db()
