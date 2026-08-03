import csv

class DataCreator:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            return list(csv_reader)

