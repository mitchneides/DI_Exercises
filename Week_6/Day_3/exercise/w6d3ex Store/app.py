from flask import Flask, render_template, redirect, flash, url_for

from flask import request
from forms import *
from new_item_form import *

import db
import cart

import random,string

app = Flask(__name__)

def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))

app.config['SECRET_KEY'] = randomword(256)


@app.route('/')
def home():
    return render_template('home.html')


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


@app.route('/add_new_shit', methods=('GET', 'POST'))
def add_new_shit():
    new_item_form = New_Item_Form()

    if request.method == 'GET':
        return render_template('new_shit.html', form=new_item_form)

    if request.method == 'POST' and new_item_form.validate():
        name = new_item_form.name.data
        price = new_item_form.price.data
        price = int(price)
        stock = new_item_form.amount.data
        stock = int(stock)
        image = new_item_form.image.data

        new_item_dict = {
            'id': None,
            'name': name,
            'price': price,
            'stock': stock,
            'image': image
        }

        products = db.load_database()
        new_id = db.get_max_id() + 1
        new_item_dict['id'] = new_id
        products.append(new_item_dict)
        db.update_db(products)

        return redirect(f'/product_details/{new_id}')


@app.route('/product_details/<int:product_id>')
def product_details(product_id):
    products = db.load_database()
    return render_template('product_details.html', product=products[product_id])


@app.route('/buy/<int:product_id>')
def buy(product_id):
    products = db.load_database()
    products[product_id]['stock'] -= 1
    db.update_db(products)

    new_item = {}
    new_item['name'] = products[product_id]['name']
    new_item['price'] = products[product_id]['price']

    user_cart = cart.load_cart()
    user_cart.append(new_item)
    cart.update_cart(user_cart)

    flash("Your item has been added to your cart!", 'flash-success')
    flash("NOTE: Your order is shipping from a corona country.", 'flash-warning')

    return redirect(f'/product_details/{product_id}')


@app.route('/view_cart')
def view_cart():
    check_cart = cart.load_cart()
    total = cart.get_balance()
    return render_template('cart.html', cart=check_cart, balance=total)






if __name__ == '__main__':
    app.run(debug=True)