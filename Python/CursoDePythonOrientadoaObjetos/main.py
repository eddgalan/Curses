
class Book:
    def __init__(self, title, author, isbn, available: bool):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = available

    def __str__(self):
        return f"Book: {self._title} - {self._author} - {self._isbn} - Available: {self._available}"

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

my_book = Book("100 anios de soledad", "Gabriel Garcia Marquez", "1234567890", True)
my_book_ = Book("El principito", "Saint-Exupery", "1234567891", True)

collection = [my_book, my_book_]

for book in collection:
    print(book)

my_book.change_availability()
print(my_book)

my_book.borrow_book()
my_book_.borrow_book()

print(my_book.title)
print(my_book.available)
my_book.available = True
print(my_book.available)