import json

def create_market_db(dst_file='market_db.json'):
    products = [
        {
            'id': 0,
            'category': 'Home',
            'product': 'Bed',
            'size': 'Full',
            'price': 500,
            'qty': 4,
            'condition': 'Gently-used',
            'description': 'Very comfortable and in great condition!',
            'image': 'bed.jpeg'
        },

        {
            'id': 1,
            'category': 'Home',
            'product': 'Couch',
            'size': 'Large',
            'price': 0,
            'qty': 3,
            'condition': 'New',
            'description': 'Brand new, L-shaped couch for donation to a lone-soldier',

            'image': 'couch.jpg'
        },

        {
            'id': 2,
            'category': 'Kitchen',
            'product': 'Cooking Supplies',
            'size': None,
            'price': 0,
            'qty': 5,
            'condition': 'Used',
            'description': 'We have a large collection of kitchen supplies/tools that we would like to donate to anyone in need',

            'image': 'kitchen.jpg'
        },

        {
            'id': 3,
            'category': 'Games',
            'product': 'PS4',
            'size': '500 GB',
            'price': 1800,
            'qty': 5,
            'condition': 'New - In original box',
            'description': 'New, unopened 500 PS4s',

            'image': 'ps4.jpeg'
        },

        {
            'id': 4,
            'category': 'Cars',
            'product': 'Kia Seltos',
            'size': 'Medium',
            'price': 16000,
            'qty': 1,
            'condition': 'Good',
            'description': 'Great, dependable car. Seats 5',

            'image': 'car.jpeg'
        }
    ]

    with open(dst_file, 'w') as f:
        json.dump(products, f)


def load_market_db(src_file='market_db.json'):
    with open(src_file, 'r') as f:
        products = json.load(f)
    return products

def update_market_db(new_product, src_file='market_db.json'):
    with open(src_file, 'w') as f:
        json.dump(new_product, f)

def get_next_id():
    all_products = load_market_db()
    max_id = 0
    for product in all_products:
        id = product['id']
        if id > max_id:
            max_id = id
    max_id += 1
    return max_id



if __name__ == "__main__":
    create_market_db()