class Order:
    global_discount = 10

    def __init__(self, amount):
        self.amount = amount

    @classmethod
    def update_global_discount(cls, discount):
        cls.global_discount = discount
        print('Global discount updated to', cls.global_discount, '%')
