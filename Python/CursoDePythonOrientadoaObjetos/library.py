class Library:
    def __init__(self, name):
        self._name = name
        self._books = []
        self._users = []

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, value):
        self._books = value

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        self._users = value

    @property
    def available_books(self):
        return [
            book.title
            for book in self._books
            if book.available
        ]
