class Library:
    def return_book(user_id, book_isbn):
        for book in user_id.borrowed_books:
            if book.ISBN == book_isbn:
                user_id.borrowed_books.romove(book)
                book.is_available = True
        
    def list_available_books():
        for book in self.list_of_books:
            print(str(book))
            
    def search_book(title=None, author=None):
        return [str(book) for book in self.list_of_book if book.title == title or book.author == author]
