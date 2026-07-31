add = lambda x, y: x + y
print(add(1, 2))

multiply = lambda x, y: x * y
print(multiply(2, 3))

# Cuadrado de cada número de la lista
numbers = range(1, 11)
squared = list(map(lambda x: x ** 2, numbers))

print("Cuadrados: ", squared)

# Obtener números pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Pares: ", even_numbers)
