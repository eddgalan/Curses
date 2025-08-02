import json
from datetime import datetime


class JsonFileManager:
    def __init__(self, filename="products.json"):
        self.filename = filename

    def __str__(self):
        return f"Filename: {self.filename}"

    def show_all_file_content(self):
        """
        Reads and displays the contents of a JSON file stored in the given filename.

        :param self: Represents the instance of the object, allowing access to
            attributes and other methods within the class.
        :raises FileNotFoundError: If the file specified by `self.filename` does not
            exist or cannot be found.
        :raises json.JSONDecodeError: If the file content is not a valid JSON.
        """
        with open(self.filename, mode="r", newline="", encoding="utf-8") as file:
            json_file = json.load(file)
            for product in json_file:
                print(product)

    def show_all_file_content_main_fields(self):
        """
        Reads the content of a specified JSON file and outputs specific fields
        ('name' and 'price') for each product listed in the file.

        :param self: Represents the instance of the class.

        :raises FileNotFoundError: If the specified file does not exist.
        :raises json.JSONDecodeError: If the file content is not valid JSON.

        :return: None
        """
        with open(self.filename, mode="r", newline="", encoding="utf-8") as file:
            json_file = json.load(file)
            for product in json_file:
                print(f"Product: {product['name']} | Price: {product['price']}")

    def add_new_product(self):
        """
        Adds a new product to the product list stored in a JSON file.

        This method prompts the user for the product's name, price, quantity, brand,
        and category.

        :raises FileNotFoundError:
            If the file specified by `self.filename` does not exist.
        :raises json.JSONDecodeError:
            If the file contains invalid JSON.
        :param self: Instance of the class that invokes this method (assumes the
            instance has a `filename` attribute indicating the path to the JSON file).

        :return: None
        """
        name = input("Type the product name: ")
        price = input("Type the product price: ")
        quantity = input("Quantity: ")
        brand = input("Type the brand: ")
        category = input("Type the product category: ")
        entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_product = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "brand": brand,
            "category": category,
            "entry_date": entry_date,
        }

        with open(self.filename, mode="r") as file:
            products = json.load(file)
        products.append(new_product)

        with open(self.filename, mode="w") as file:
            json.dump(products, file, indent=4)
        print("Product added successfully!")
