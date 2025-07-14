my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print(type(my_iterator))

# Iterador con Texto
text = "Hello World"
iter_text = iter(text)

for char in iter_text:
    print(char)

# Iterador para números impares
limit = 10
odd_iter = iter(range(1, limit + 1, 2))

for num in odd_iter:
    print(num)

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)
