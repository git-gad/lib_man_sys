from book import Book

class User:
    def __init__(self,name, id):
        self.name=name
        self.id=id
        self.borrowed_books=[]

    def __str__(self):
        return f"the name is:{self.name}\n His ID card is:{self.id}\n borrowed_books is:{self.borrowed_books}"










