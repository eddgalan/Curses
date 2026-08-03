from typing import Protocol

class BookProtocol(Protocol):
    def borrow_book(self) -> str:
        """Borrow a book"""

    def return_book(self) -> str:
        """Return a book"""

    def calculate_duration(self) -> str:
        """Calculate the duration of a book"""


class PhysicalBook(BookProtocol):
    def calculate_duration(self):
        return "7 days"


class DigitalBook(BookProtocol):
    def calculate_duration(self):
        return "14 days"


class Book:
    def __init__(self, title, author, isbn, available: bool):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = available

    def __str__(self):
        return f"Book: {self._title} - {self._author} - {self._isbn} - Available: {self._available}"

    def __repr__(self):
        return self.__str__()

    @property
    def title(self):
        return self._title

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    def borrow_book(self):
        if self._available:
            self._available = False
            print(f"Libro {self._title} prestado")
        else:
            print(f"Libro {self._title} no disponible")

    def change_availability(self):
        self._available = not self._available