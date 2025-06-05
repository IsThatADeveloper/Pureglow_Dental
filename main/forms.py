from main import app
from flask import Flask,  render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('instance/appointments.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments
                      (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, email TEXT, service TEXT, number TEXT, date TEXT, time TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        number = request.form['number']
        service = request.form['service']
        datetime_str = request.form['datetime']
        datetime_obj = datetime.fromisoformat(datetime_str)
        date = datetime_obj.strftime('%Y-%m-%d')
        time = datetime_obj.strftime('%H:%M:%S')

        conn = sqlite3.connect('instance/appointments.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO appointments (firstname, lastname, email, service, number, date, time)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''', (firstname, lastname, email, service, number, date, time))
        conn.commit()
        conn.close()
        return redirect(url_for('book_appointment'))

    return render_template('home.html')