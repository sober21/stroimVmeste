from flask import render_template, url_for
from app import app


@app.route('/')
def index():
    return render_template('index.html', title='Главная')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='О нас')


@app.route('/price')
def price():
    return render_template('price.html', title='Цены')
