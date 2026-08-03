from exceptions import UserNotFoundError


class Library:
    def __init__(self, name, books=None, users=None):
        if users is None:
            users = []
        if books is None:
            books = []
        self._name = name
        self._books = books
        self._users = users

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
            book
            for book in self._books if book.available
        ]

    def search_user(self, user_id):
        for user in self._users:
            if user.id == user_id:
                return user
        raise UserNotFoundError(f"El usuario con el Id: {str(user_id)} no se encuentra en la biblioteca")
