a = [1, 2, 3, 4, 5]
b = a
print(a)
print(b)

del a[0]
print(a)
print(b)
print(id(a), id(b))

c = a[:]
print(id(c))

a.append(6)
print(a)
print(b)
print(c)
