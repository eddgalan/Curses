
class Book:
    def __init__(self, title, author, isbn, available: bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"Libro: {self.title} - {self.author}"

my_book = Book("100 anios de soledad", "Gabriel Garcia Marquez", "1234567890", True)
my_book_ = Book("El principito", "Saint-Exupery", "1234567891", False)

collection = [my_book, my_book_]

for book in collection:
    print(book)
