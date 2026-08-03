import json
from book import Book
from datetime import datetime
from library import Library
from user import Student, Teacher


class JsonExporter:
    def __init__(self, file="library.json") -> None:
        self.file = file

    def save(self, library):
        data = {
            "name": library.name,
            "users": [
                user.to_dict() for user in library.users
            ],
            "books": [
                book.to_dict() for book in library.books
            ],
            "date": datetime.now().isoformat(),
        }
        with open(self.file, mode='w', newline='', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load(self):
        with open(self.file, mode='r', newline='', encoding='utf-8') as file:
            data = json.load(file)

        #print("data: " + str(data))
        library = Library(data["name"])

        books = []
        for book_data in data["books"]:
            book = Book(**book_data)
            books.append(book)
        library.books = books

        users = []
        for user_data in data["users"]:
            if 'course' in user_data:
                user = Student(**user_data)
            else:
                user = Teacher(**user_data)
            users.append(user)
        library.users = users

        return library