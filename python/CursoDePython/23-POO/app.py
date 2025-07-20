class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Función que saluda
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.name}")

person1 = Person('Edson', 28)
person2 = Person('Sara', 25)

person1.greet()
person2.greet()
