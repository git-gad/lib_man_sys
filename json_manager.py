import json
from Library import Library
from book import Book
from user import User


def import_data_from_json_file(file_name: str, lib: Library):
    with open(file_name, 'r') as f:
        data = json.load(f)

        users = data["users"]
        books = data["books"]

        for user in users:
            _user=User(user["name"],user["id"])
            lib.users.append(_user)

        for book in books:
            _book=Book(book["title"],book["author"],book["ISBN"])
            lib.books.append(_book)


def export_data_to_json_file(file_name: str, lib: Library):
    user_arr=[]
    book_arr=[]

    for user in lib.users:
        user_dict ={
            "name":user.name,
            "id": user.id
        }
        user_arr.append(user_dict)

    for book in lib.books:
        book_dict={
            "ISBN": book.ISBN,
            "author": book.author,
            "title": book.title
        }
        book_arr.append(book_dict)

    data_lib={
        "users":user_arr,
        "books":book_arr
    }

    with open(file_name, 'w') as f:
        json.dump(data_lib, f, ensure_ascii=False,indent=4)
