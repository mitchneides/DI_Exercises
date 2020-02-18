from flask import Flask
import datetime
from flask import render_template

from Week_6.Day_2.onlineStore import db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/greeting')
def greeting():
    now = datetime.datetime.now()
    hour = now.hour
    if 6<=hour<12:
        return 'Good morning'
    elif 12<=hour<17:
        return 'Good afternoon'
    elif 17<=hour<21:
        return 'Good evening'
    else:
        return 'Good night'


@app.route('/')
def home():
    html_home = render_template('home.html')
    return html_home

@app.route('/products')
def products(): #CONTROLLER

    products = db.load_database() #MODEL

    return render_template('home.html', products=products) #VIEW


@app.route('/product-details/<product>')
def product_details(product):
    html_product_details = render_template('product_details.html')
    return html_product_details


from flask import request
from Week_6.Day_2.onlineStore.forms import *

@app.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if request.method == 'GET':
        return render_template('loginForm.html', form=login_form)

    if request.method == 'POST' and login_form.validate():
        name = login_form.name.data
        password = login_form.password.data
        info = login_form.info.data

        if name == "Jonathan" and password == "horse":
            return '<h1>Welcome Jon</h1>'

        else:
            return "<h1>Access denied</h1>"

    else:
        return "<h1>Failed Validation</h1>"






if __name__ == '__main__':
    app.run(debug=True)
