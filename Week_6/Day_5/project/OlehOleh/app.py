from flask import Flask, render_template, redirect, flash, request
import random,string
from sign_up_form import *
from sign_in_form import *
import user_db
import cart
import market_db

app = Flask(__name__)

def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))

app.config['SECRET_KEY'] = randomword(256)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sign_up', methods=('GET', 'POST'))
def sign_up():
    sign_up_form = Sign_Up_Form()

    if request.method == 'GET':
        return render_template('sign_up.html', form=sign_up_form)

    if request.method == 'POST' and sign_up_form.validate():
        name = sign_up_form.name.data
        email = sign_up_form.email.data
        password = sign_up_form.password.data

        all_users = user_db.load_user_db()
        id = user_db.get_next_id()
        print(f"id {id}")

        new_user = {"name": name, "email": email, "password": password, "id": id}

        all_users.append(new_user)
        user_db.update_user_db(all_users)

        return redirect('/market')

    else:
        return "<h1>Failed Validation - Go back to try again.</h1>"


@app.route('/sign_in', methods=('GET', 'POST'))
def sign_in():
    sign_in_form = Sign_In_Form()

    if request.method == 'GET':
        return render_template('sign_in.html', form=sign_in_form)

    if request.method == 'POST' and sign_in_form.validate():
        email = sign_in_form.email.data
        password = sign_in_form.password.data

        all_users = user_db.load_user_db()
        for user in all_users:
            if user['email'] == email and user['password'] == password:
                return redirect('/market')
                # ////////////////////////////////////////////////////////// update later //////////////////////////////////////////
        return "<h1>Incorrect Credentials - Go back to try again.</h1>"

    else:
        return "<h1>Failed Validation</h1>"


@app.route('/market')
def market():
    products = market_db.load_market_db()
    return render_template('market.html', products=products)


@app.route('/product/<int:id>')
def product(id):
    products = market_db.load_market_db()
    for thing in products:
        if thing['id'] == id:
            item = thing
    return render_template('product.html', product=item)


@app.route('/buy/<int:id>')
def buy(id):
    products = market_db.load_market_db()
    for thing in products:
        if thing['id'] == id:
            thing['qty'] -= 1
    market_db.update_market_db(products)
    return redirect(f'/product/{id}')



@app.route('/my_cart')
def my_cart():
    check_cart = cart.load_cart()
    total = cart.get_balance()
    return render_template('cart.html', cart=check_cart, balance=total)





if __name__ == '__main__':

    app.run(debug=True)