import json

# json.dump takes a string (formatted like js) and outputs json notation
# json.load takes json and formats it back to python

# there is also json.dumps and json.loads

# writing to/reading files:
    # with open('jon.txt', 'r') as f:
    #     date = f.read()


def create_database(dst_file='database/my_file.json'):
    data = [
        {
            'name': 'iphone 9',
            'price': 799,
            'instock': True
        },

        {
            'name': 'Macbook Pro',
            'price': 4799,
            'instock': False
        },

        {
            'name': 'Apple Watch',
            'price': 10799,
            'instock': True
        },

        {
            'name': 'Apple stand pro',
            'price': 99999,
            'instock': True
        },
    ]
    with open(dst_file, 'w') as file_obj:
        json.dump(data, file_obj, indent=4)


def load_database(src_file='database/my_file.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(file_obj)
    return data




