from flask import Flask, render_template, redirect

import db

import random,string

app = Flask(__name__)

def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))

app.config['SECRET_KEY'] = randomword(256)


@app.route('/')
def home():
    return render_template('home.html')

from flask import request
from forms import *

@app.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=login_form)

    if request.method == 'POST' and login_form.validate():
        name = login_form.name.data
        password = login_form.password.data

        if name == "Ricky" and password == "dirtydancin":
            return redirect('/add_new_shit')
        else:
            return "<h1>Access Denied</h1>"

    else:
        return "<h1>Failed Validation</h1>"


@app.route('/products')
def products():
    products = db.load_database()
    return render_template('products.html', products=products)


@app.route('/add_new_shit')
def add_new_shit():
    pass
# ///////////////////////////////// pick up from here ////////////////////////////////


@app.route('/product_details/<int:product_id>')
def product_details(product_id):
    products = db.load_database()
    return render_template('product_details.html', product=products[product_id])


@app.route('/buy/<int:product_id>')
def buy(product_id):
    products = db.load_database()
    products[product_id]['stock'] -= 1
    db.update_db(products)
    return redirect(f'/product_details/{product_id}')









if __name__ == '__main__':
    app.run(debug=True)