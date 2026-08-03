import json
from datetime import datetime

class JsonExporter:
    def __init__(self, file="library.json") -> None:
        self.file = file

    def save(self, library):
        data = {
            "name": library.name,
            "users": [
                user.__dict__
                for user in library.users
            ],
            "books": [
                book.__dict__
                for book in library.books
            ],
            "date": datetime.now().isoformat(),
        }
        with open(self.file, mode='w', newline='', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
