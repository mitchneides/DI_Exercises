import json

def create_database(dst_file='my_file.json'):
    data = [
        {
            'id': 0,
            'name': 'Clearing Stick',
            'price': 18,
            'stock': 4,
            'image': 'stick.jpeg'
        },

        {
            'id': 1,
            'name': 'Rick Shirt',
            'price': 12,
            'stock': 8,
            'image': 'shirt.jpeg'
        },

        {
            'id': 2,
            'name': 'Conky',
            'price': 106,
            'stock': 3,
            'image': 'conky.jpeg'
        },

        {
            'id': 3,
            'name': 'Chicken Tenders (the good kind)',
            'price': 9,
            'stock': 5,
            'image': 'chicken.jpeg'
        },

        {
            'id': 4,
            'name': 'Legally Purchased BBQ',
            'price': 225,
            'stock': 5,
            'image': 'bbq.jpeg'
        }
    ]

    with open(dst_file, 'w') as f:
        json.dump(data, f)


def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data


def update_db(products, src_file='my_file.json'):
    with open(src_file, 'w') as f:
        json.dump(products, f)

