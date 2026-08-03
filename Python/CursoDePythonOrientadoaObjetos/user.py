from typing import Protocol
from exceptions import TitleInvalidError

class RequesterProtocol(Protocol):
    def borrow_book(self, title: str) -> str:
        """
        Allows the user to borrow a book from the library by its title.
        """
        ...

class User:
    def __init__(self, name, user_id):
        self._name = name
        self._id = user_id
        self._books_borrowed = []

    def __str__(self):
        return f"User: {self._name} - ID: {self._id}"

    def __repr__(self):
        return self.__str__()

    @property
    def id(self):
        return self._id

    def borrow_book(self, book):
        return f"El usuario {self._name} ha alquilado el libro {book.title}"


class Student(User):
    def __init__(self, name, user_id, course):
        super().__init__(name, user_id)
        self._course = course
        self._books_limit = 3

    def borrow_book(self, title):
        if not title:
            raise TitleInvalidError("Title should not be empty")

        if len(self._books_borrowed) < self._books_limit:
            self._books_borrowed.append(title)
            return f"El usuario {self._name} ha alquilado el libro {title}"
        else:
            return f"No puedes alquilar mas libros, limite alcanzado. Limite: {self._books_limit}"


class Teacher(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.books_limit = None

    def borrow_book(self, title):
        self._books_borrowed.append(title)
        return f"El usuario {self._name} ha alquilado el libro {title}"

