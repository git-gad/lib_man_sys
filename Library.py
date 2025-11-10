from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self,book:Book):
        self.books.append(book)

    def add_users(self,user:User):
        self.users.append(user)

    def borrow_book(self, user_id, book_isbn):
        for book in self.books:
            if book.ISBN == book_isbn:
                book.is_available = False
                for user in self.users:
                    if user.id == user_id:
                        user.borrowed_books.append(book)
                        return






