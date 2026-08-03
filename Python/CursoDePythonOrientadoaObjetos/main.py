from book import Book
from exceptions import LibraryError, BookNotAvailableError
from library import Library
from user import Student, Teacher, RequesterProtocol


student_1 = Student("Juan", 123, "Python")
student_2 = Student("Maria", 456, "Java")
teacher = Teacher("Pedro", 456)
users: list[RequesterProtocol] = [student_1, student_2, teacher]


my_book_1 = Book("100 anios de soledad", "Gabriel Garcia Marquez", "1234567890", True)
my_book_2 = Book("El principito", "Saint-Exupery", "1234567891", True)
my_book_3 = Book("El quijote de la mancha", "Miguel de Cervantes Saavedra", "1234567892", False)


library = Library("Mi biblioteca")
library.books = [my_book_1, my_book_2, my_book_3]

try:
    print(student_1.borrow_book(None))
except LibraryError as e:
    print(f"No se puede llevar el libro. '{e}'")
    print(f"Error Type: {type(e)}")

try:
    my_book_3.borrow_book()
except BookNotAvailableError as e:
    print(f"No se puede llevar el libro. '{e}'")
    print(f"Error Type: {type(e)}")
