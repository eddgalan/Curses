from book import Book
from library import Library
from user import Student, Teacher, RequesterProtocol


student_1 = Student("Juan", 123, "Python")
student_2 = Student("Maria", 456, "Java")
teacher = Teacher("Pedro", 456)
users: list[RequesterProtocol] = [student_1, student_2, teacher]


my_book_1 = Book("100 anios de soledad", "Gabriel Garcia Marquez", "1234567890", True)
my_book_2 = Book("El principito", "Saint-Exupery", "1234567891", True)
my_book_3 = Book("El quijote de la mancha", "Miguel de Cervantes Saavedra", "1234567892", True)


library = Library("Mi biblioteca")
library.books = [my_book_1, my_book_2, my_book_3]
print(library.available_books)
print(library.books)
