from book import Book
from user import User
from library import Library
from json_manager import *

if __name__ == '__main__':
    l = Library()
    books = load_json_books()  #reads json file and puts list of dictionaries of books in variable
    users = load_json_users()  #reads json file and puts list of dictionaries of users in variable
    for book in books:   
        b = Book(book['title'], book['author'], book['ISBN'])   #create Book instance and add it to book list
        l.add_book(b)
    for user in users:
        u = User(user['name'], user['id'])  #crate User instace and add it to users list 
        l.add_user(user)




