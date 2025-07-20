class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'{self.brand} {self.model} vendido con exito')
        else:
            print(f'{self.brand} {self.model} NO está disponible')

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError('Este método debe ser implementado en la clase hija')

    def stop_engine(self):
        raise NotImplementedError('Este método debe ser implementado en la clase hija')

