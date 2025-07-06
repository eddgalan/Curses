to_do = ["Wakeup", "Breakfast", "Lunch", "Dinner", "Sleep"]
print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
print("Type of numbers: ", type(numbers))

mix = [1, "dos", 3.1416, True, [1, 2, 3], { "a": 1, "b": 2}]
print(mix)

print("Count of elements: ", len(mix))
print("First element: ", mix[0])
print("Last element: ", mix[-1])

print(mix[0:2])
print(mix[2:])

mix.append(False)
print(mix)

mix.append([1, 2, 3])
print(mix)

mix.insert(1, "insert")
print(mix)

print(mix.index(False)) # Busca la primera aparición de un elemento

# Operaciones numéricas
numbers = [1, 87, 456, 44.11, 90]
print(numbers)
print("Min: ", min(numbers))
print("Max: ", max(numbers))
print("Sum: ", sum(numbers))
print("Average: ", sum(numbers) / len(numbers))

del numbers[-1]
print(numbers)

del numbers[:2]
print(numbers)

del numbers[:]
print(numbers)

del numbers
print(numbers)
