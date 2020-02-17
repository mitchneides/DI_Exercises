from flask import Flask
import datetime
from flask import render_template

from Week_6.Day_2.onlineStore import db


app = Flask(__name__)

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




if __name__ == '__main__':
    app.run(debug=True)
