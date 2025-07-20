from vehicle import Vehicle

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El motor del camión {self.brand} está en marcha'
        else:
            return f'El camión {self.brand} NO está disponible'

    def stop_engine(self):
        if self.is_available:
            return f'El motor del camión {self.brand} se ha detenido'
        else:
            return f'El camión {self.brand} NO está disponible'