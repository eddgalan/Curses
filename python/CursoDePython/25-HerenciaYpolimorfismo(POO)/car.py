from vehicle import Vehicle

class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f'El motor del coche {self.brand} está en marcha'
        else:
            return f'El coche {self.brand} NO está disponible'

    def stop_engine(self):
        if self.is_available:
            return f'El motor del coche {self.brand} se ha detenido'
        else:
            return f'El coche {self.brand} NO está disponible'
