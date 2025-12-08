from ecommerce.inventory import add_product, remove_product
from ecommerce.sales import process_sale

if __name__ == "__main__":
    add_product("Laptop", 1000)
    add_product("Mouse", 50)
    remove_product("Laptop")
    process_sale("Laptop", 2)
