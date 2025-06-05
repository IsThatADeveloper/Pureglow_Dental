from flask import Flask, render_template, url_for, flash, redirect, request
from main import app
import re
import sqlite3
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        service = request.form['service']
        number = request.form['number']
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
        flash('Appointment made', 'success')
        return redirect(url_for('book_appointment', success=True))
    
    success = request.args.get('success') == 'True'
    return render_template('home.html', success=success)

@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/appointment")
def appointment():
    return render_template('pages/appointment.html', title='Appointment')

@app.route("/about")
def about():
    return render_template('pages/about.html', title='About Us')

@app.route("/contact")
def contact():
    return render_template('pages/contact.html', title='Contact Us')
