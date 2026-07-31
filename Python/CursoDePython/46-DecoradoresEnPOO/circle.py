class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.14 * self._radius**2

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError('El radio no puede ser negativo')
        self._radius = value


circle = Circle(5)
print(circle.area)
print(circle.radius)

circle.radius = 10
print(circle.area)
print(circle.radius)

circle.radius = -10
