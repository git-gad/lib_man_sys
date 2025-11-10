import json

from Library import Library

def json_management_books():
    l = Library()
    with open('data.json', 'r') as f:
        data = json.load(f)
        l.books = data["books"]
        return l.books

def json_management_users():
    l = Library()
    with open('data.json', 'r') as f:
        data = json.load(f)
        l.users = data["users"]
        return l.users


print(json_management_books())
print(json_management_users())
