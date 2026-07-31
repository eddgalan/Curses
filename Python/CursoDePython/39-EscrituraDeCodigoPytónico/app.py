numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    square = number**2
    squares.append(square)

print(squares)

# Usando list comprehension
squares = [number**2 for number in numbers]
print(squares)
