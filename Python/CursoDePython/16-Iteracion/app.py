numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print(i)
for i in range(10):
    print(i)
for i in range(3, 10):
    print(i)

fruits = ['platano', 'manzana', 'pera', 'uva', 'fresa', 'mango', 'limón', 'mandarina']
print("Fruits:", fruits)

citrus = ['limón', 'fresa', 'mandarina']
print("Citrus:", citrus)

for fruit in fruits:
    if fruit in citrus:
        print(fruit)

x = 0
while x < len(fruits):
    if fruits[x] in citrus:
        print(fruits[x])
        break
    x += 1
