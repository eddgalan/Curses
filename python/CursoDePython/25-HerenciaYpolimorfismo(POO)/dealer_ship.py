from vehicle import Vehicle
from customer import Customer

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f'El vehículo {vehicle.brand} ha sido agregado al inventario')

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'El cliente {customer.name} ha sido registrado')

    def show_inventory(self):
        print('Vehículos disponibles en la tienda:')
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f'- {vehicle.brand} ({vehicle.get_price()})')