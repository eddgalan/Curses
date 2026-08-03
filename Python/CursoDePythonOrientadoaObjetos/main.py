from book import Book
from data.books_creator import BooksCreator
from data.json_exporter import JsonExporter
from exceptions import UserNotFoundError, BookNotFoundError
from library import Library
from user import Student, Teacher, RequesterProtocol

# result = Library.validate_isbn("1234567890")
# print(f"Isbn valid: {result}")
#
# not_available_book = Book.create_not_available("Prueba", "Autor de prueba", "1234567899")
# print(not_available_book)

book_importer = BooksCreator("data/books_catalog.csv")
books = book_importer.create()

student_1 = Student("Juan", 123, "Python")
student_2 = Student("Maria", 456, "Java")
teacher = Teacher("Pedro", 789)
users: list[RequesterProtocol] = [student_1, student_2, teacher]

library = Library(
    "Mi biblioteca",
    books,
    users
)

json_exporter = JsonExporter()
json_exporter.save(library)

library_backup = json_exporter.load()

print("Bienvenido a la biblioteca")
print(f"Available Books:")
for book in library.available_books:
    print(f"  - {book.title} - {book.author}")


user_id = int(input("Ingrese el id del usuario: "))
try:
    user = library.search_user(user_id)
except UserNotFoundError as e:
    print(f"El usuario con id {user_id} no existe")
    user = None
print(user)


title = input("Ingrese el titulo del libro: ")
try:
    book = library.search_book(title)
    print(book)
except BookNotFoundError as e:
    print(e)
    book = None

if user and book:
    r_user = user.borrow_book(book.title)
    print(r_user)

    r_book = book.borrow_book()
    print(r_book)
