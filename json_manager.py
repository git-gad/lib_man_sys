import json

def load_json_books() -> list:
    with open('data.json', 'r') as f:
        data = json.load(f)
    return [data['books']]
    
def load_json_users() -> list:
    with open('data.json', 'r') as f:
        data = json.load(f)
    return [data['users']]

def dump():
    pass