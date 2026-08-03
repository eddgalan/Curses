from book import Book
from exceptions import LibraryError, BookNotAvailableError, UserNotFoundError
from library import Library
from user import Student, Teacher, RequesterProtocol


student_1 = Student("Juan", 123, "Python")
student_2 = Student("Maria", 456, "Java")
teacher = Teacher("Pedro", 789)
users: list[RequesterProtocol] = [student_1, student_2, teacher]


my_book_1 = Book("100 anios de soledad", "Gabriel Garcia Marquez", "1234567890", True)
my_book_2 = Book("El principito", "Saint-Exupery", "1234567891", True)
my_book_3 = Book("El quijote de la mancha", "Miguel de Cervantes Saavedra", "1234567892", False)

library = Library(
    "Mi biblioteca",
    [my_book_1, my_book_2, my_book_3],
    users
)


print("Bienvenido a la biblioteca")
print("Users: " + str(library.users))
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
