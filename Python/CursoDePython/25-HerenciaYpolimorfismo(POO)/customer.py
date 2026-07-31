from vehicle import Vehicle

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.is_available:
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f'El vehículo {vehicle.brand} NO está disponible')

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            avaliability = 'Disponible'
        else:
            avaliability = 'No disponible'
        print(f'El vehículo {vehicle.brand} está {avaliability} y cuesta {vehicle.get_price()}')
