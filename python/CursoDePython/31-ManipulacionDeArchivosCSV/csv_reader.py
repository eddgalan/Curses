import csv
from datetime import datetime

class CsvReader:
    def __init__(self, filename='products.csv'):
        self.filename = filename

    def __str__(self):
        return f'Filename: {self.filename}'

    def show_all_file_content(self):
        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                print(row)

    def show_all_file_content_main_fields(self):
        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                print(f"Product: {row['name']} | Price: {row['price']}")

    def add_new_product(self):
        name = input("Type the product name: ")
        price = input("Type the product price: ")
        quantity = input("Quantity: ")
        brand = input("Type the brand: ")
        category = input("Type the product category: ")
        entry_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(self.filename, mode='a', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=['name', 'price', 'quantity', 'brand', 'category', 'entry_date'])
            csv_writer.writerow({
                'name': name,
                'price': price,
                'quantity': quantity,
                'brand': brand,
                'category': category,
                'entry_date': entry_date
            })
        print('Product added successfully!')
