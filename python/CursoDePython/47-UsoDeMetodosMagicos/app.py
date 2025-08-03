from person import Person

p1 = Person("Juan", 25)
p2 = Person("Pedro", 30)
p3 = Person("Juan", 25)

print(p1)
print(repr(p1))

print(f"¿{p1.name} es igual a {p2.name}? {p1 == p2}")
print(f"¿{p1.name} es igual a {p3.name}? {p1 == p3}")

print(f"¿{p1.name} es menor que {p2.name}? {p1 < p2}")

print(f"Suma de edades de {p1.name} y {p2.name} es: {p1 + p2}")
