from bike import Bike
from car import Car
from truck import Truck
from customer import Customer
from dealer_ship import Dealership

car1 = Car('Toyota', 'Corolla', 20000)
car2 = Car('Toyota', 'Highlander', 30000)
car3 = Car('Toyota', 'Camry', 40000)

bike1 = Bike('Yamaha', 'Corolla', 7000)
bike2 = Bike('Yamaha', 'Yaris', 10000)

truck1 = Truck('Volvo', 'MT-07', 15000)

customer1 = Customer('Edson')

dealership1 = Dealership()
vehicles = [car1, car2, car3, bike1, bike2, truck1]

for vehicle in vehicles:
    dealership1.add_vehicle(vehicle)

dealership1.show_inventory()

# Cliente consulta vehículo
customer1.inquire_vehicle(truck1)

# Cliente compra auto
customer1.buy_vehicle(truck1)

dealership1.show_inventory()

customer1.purchased_vehicles()
