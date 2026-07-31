
class Book:
    def __init__(self, title, author, isbn, available: bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"Book: {self.title} - {self.author} - {self.isbn} - Available: {self.available}"

    def lend_book(self):
        if self.available:
            self.available = False
            print(f"Libro {self.title} prestado")
        else:
            print(f"Libro {self.title} no disponible")

    def change_availability(self):
        self.available = not self.available

my_book = Book("100 anios de soledad", "Gabriel Garcia Marquez", "1234567890", True)
my_book_ = Book("El principito", "Saint-Exupery", "1234567891", True)

collection = [my_book, my_book_]

for book in collection:
    print(book)

my_book.change_availability()
print(my_book)

my_book.lend_book()
my_book_.lend_book()