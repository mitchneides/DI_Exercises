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


    

if __name__ == '__main__':
    app.run(debug=True)
