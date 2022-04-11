from flask import render_template

from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Homepage')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/products')
def products():
    return render_template('products.html', title='Products')


@app.route('/basket')
def basket():
    return render_template('basket.html', title='Basket')


