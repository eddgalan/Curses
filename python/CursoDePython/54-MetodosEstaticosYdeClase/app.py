from order import Order
from order_1 import Order as Order1

if __name__ == "__main__":
    print (Order.calculate_tax(150, 16))

    Order1.update_global_discount(50)
