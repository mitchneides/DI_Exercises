from flask import Flask, render_template
from exerciseStore import db

app = Flask(__name__)


@app.route('/')
def home():
    html_home = render_template('home.html')
    return html_home


@app.route('/products')
def products():
    products = db.load_database()
    html_products = render_template('products.html', products=products)
    return html_products


@app.route('/products/<product_id>')
def product_by_id(product_id):
    products = db.load_database()
    specific_item = {}
    for item in products:
        if item['ProductId'] == product_id:
            specific_item = item

    html_product_id = render_template('product_id.html', product=specific_item)
    return html_product_id


@app.route('/search/by-category/<category>')
def search_by_cat(category):
    products = db.load_database()
    product_list = []
    for product in products:
        if category in product['Category']:
            product_list.append(product)
    product_list = str(product_list)
    # return product_list
    # pick up from here #####################################################


@app.route('/fibonacci/<num>')
def fibonacci(num):
    num = int(num)
    list = []
    for c,digit in enumerate(range(num)):
        if digit == 0:
            list.append(0)
        elif digit == 1:
            list.append(1)
        elif digit < 0:
            return "Invalid."
        else:
            list.append(list[c-1]+list[c-2])

    return str(list)


    

if __name__ == '__main__':
    app.run(debug=True)
