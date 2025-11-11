from Library import Library
from book import Book
from input_book_user import Input_book_and_user
from json_manager import import_data_from_json_file, export_data_to_json_file
from user import User


if __name__=="__main__":
    lib = Library()
    import_data_from_json_file("data.json",lib)
    while True:
        choice = input('1. Add Book\n2. Add User\n3. Borrow Book\n'
              '4. Return Book\n5. List Available Books\n'
              '6. Search Book By Name Or Author\n7. Save & Exit\n')
        if choice == '1':
            new_book = Input_book_and_user.input_book()
            book = Book(new_book["title"],new_book["author"],new_book["ISBN"])
            lib.add_book(book)
        elif choice == '2':
            new_user = Input_book_and_user.input_user()
            user = User(new_user['name'], new_user['id'])
            lib.add_user(user)
        elif choice == '3':
            user_id = input('user id: ')
            book_isbn = input('book isbn: ')
            lib.borrow_book(user_id, book_isbn)
        elif choice == '4':
            user_id = input('user id: ')
            book_isbn = input('book isbn: ')
            lib.return_book(user_id, book_isbn)
        elif choice == '5':
            lib.list_available_books()
        elif choice == '6':
            choice2 = input('search by book or by author: (book/author')
            if choice2 == 'book':
                book_name = input('book name: ')
                lib.search_book(book_name)
            elif choice2 == 'author':
                author_name = input('author name: ')
                print(lib.search_book(author=author_name, title=None))
        elif choice == '7':
            export_data_to_json_file('data.json', lib)
            break










