class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        # Devuelve una representación amigable para el usuario
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self) -> str:
        # Devuelve una representación
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other) -> bool:
        # Compara si dos personas son iguales en función del nombre
        return self.name == other.name and self.age == other.age

    def __lt__(self, other) -> bool:
        # Compara si una persona es menor que otra en función de la edad
        return self.age < other.age

    def __add__(self, other) -> int:
        # Sobrecarga el operador + para sumar las edades de dos personas
        return self.age + other.age
