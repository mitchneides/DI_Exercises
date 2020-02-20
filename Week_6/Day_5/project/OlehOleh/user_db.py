import json

def create_user_db(dst_file='user_db.json'):
    users = [
        {
            'name': 'admin',
            'email': 'admin@oleholeh.co.il',
            'password': '1948',
            'id': 0
        }
    ]

    with open(dst_file, 'w') as f:
        json.dump(users, f)


def load_user_db(src_file='user_db.json'):
    with open(src_file, 'r') as f:
        users = json.load(f)
    return users

def update_user_db(new_user, src_file='user_db.json'):
    with open(src_file, 'w') as f:
        json.dump(new_user, f)

def get_next_id():
    all_users = load_user_db()
    max_id = 0
    for user in all_users:
        id = user['id']
        if id > max_id:
            max_id = id
    max_id += 1
    return max_id



if __name__ == "__main__":
    create_user_db()