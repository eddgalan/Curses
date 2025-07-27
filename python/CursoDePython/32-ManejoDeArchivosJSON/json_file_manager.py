import json
from datetime import datetime

class JsonFileManager:
    def __init__(self, filename='products.json'):
        self.filename = filename

    def __str__(self):
        return f'Filename: {self.filename}'

    def show_all_file_content(self):
        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            json_file = json.load(file)
            for product in json_file:
                print(product)

    def show_all_file_content_main_fields(self):
        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            json_file = json.load(file)
            for product in json_file:
                print(f"Product: {product['name']} | Price: {product['price']}")

    def add_new_product(self):
        name = input("Type the product name: ")
        price = input("Type the product price: ")
        quantity = input("Quantity: ")
        brand = input("Type the brand: ")
        category = input("Type the product category: ")
        entry_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        new_product = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'brand': brand,
            'category': category,
            'entry_date': entry_date
        }

        with open(self.filename, mode='r') as file:
            products = json.load(file)
        products.append(new_product)

        with open(self.filename, mode='w') as file:
            json.dump(products, file, indent=4)
        print('Product added successfully!')