class Input_book_and_user:
    @staticmethod
    def input_book() -> dict:
        new_book = {
            "ISBN": input("please enter ISBN:"),
            "author": input("please enter author:"),
            "title": input("please enter title:")
        }
        return new_book

    @staticmethod
    def input_user( ) -> dict:
        new_user = {
            "name": input("please enter name:"),
            "id": input("please enter id:"),
        }
        return new_user