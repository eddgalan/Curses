from typing import Protocol

class RequesterProtocol(Protocol):
    def borrow_book(self, title: str) -> str:
        """
        Allows the user to borrow a book from the library by its title.
        """
        ...

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.books_borrowed = []

    def borrow_book(self, book):
        return f"El usuario {self.name} ha alquilado el libro {book.title}"


class Student(User):
    def __init__(self, name, user_id, course):
        super().__init__(name, user_id)
        self.course = course
        self.books_limit = 3

    def borrow_book(self, title):
        if len(self.books_borrowed) < self.books_limit:
            self.books_borrowed.append(title)
            return f"El usuario {self.name} ha alquilado el libro {title}"
        else:
            return f"No puedes alquilar mas libros, limite alcanzado. Limite: {self.books_limit}"


class Teacher(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.books_limit = None

    def borrow_book(self, title):
        self.books_borrowed.append(title)
        return f"El usuario {self.name} ha alquilado el libro {title}"


student_1 = Student("Juan", 123, "Python")
student_2 = Student("Maria", 456, "Java")
teacher = Teacher("Pedro", 456)

from main import Book
book = Book("Python para iniciantes", "Pedro", "0123456789", True)

users: list[RequesterProtocol] = [student_1, student_2, teacher, book]

for user in users:
    print(user.borrow_book("Python para iniciantes"))
