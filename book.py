class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = True
        
    def __str__(self):
        return f'{self.title} from {self.author}'