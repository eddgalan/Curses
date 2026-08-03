from book import Book
from data.data_creator import DataCreator


class BooksCreator(DataCreator):
    def __init__(self, path):
        super().__init__(path)

    def create(self):
        books = self.get_data()
        books_instances = []
        for book in books:
            books_instances.append(Book(**book))
        return books_instances

