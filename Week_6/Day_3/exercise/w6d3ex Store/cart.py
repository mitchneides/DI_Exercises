import json


def create_cart(dst_file = 'my_cart.json'):
    shopping_cart = []

    with open(dst_file, 'w') as f:
        json.dump(shopping_cart, f)


def load_cart(src_file='my_cart.json'):
    with open(src_file, 'r') as f:
        the_cart = json.load(f)
    return the_cart


def update_cart(products, src_file='my_cart.json'):
    with open(src_file, 'w') as f:
        json.dump(products, f)


def get_balance():
    items = load_cart()
    balance = 0
    for item in items:
        balance += item['price']

    return balance


if __name__ == '__main__':
    create_cart()