class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f'El libro {book.title} ha sido agregado a la biblioteca')

    def add_user(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido agregado a la biblioteca')

    def show_available_books(self):
        print('Libros disponibles:')
        for book in self.books:
            if book.available:
                print(f'- {book.title} ({book.author})')
