from vehicle import Vehicle
# Herencia
class Bike(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f'La bicicleta {self.brand} está en marcha'
        else:
            return f'La bicicleta {self.brand} NO está disponible'
    # Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f'La bicicleta {self.brand} se ha detenido'
        else:
            return f'La bicicleta {self.brand} NO está disponible'
