from flask import render_template, url_for
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/naplavlyaemaya_krovlya')
def naplav():
    return render_template('naplavlyaemaya.html')


@app.route('/myagkaya_krovlya')
def myagkaya():
    return render_template('myagkaya.html')


@app.route('/price')
def price():
    return render_template('price.html')