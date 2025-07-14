x = 5
if x > 5:
    print('x es mayor a 5')
elif x == 5:
    print('x es igual a 5')
else:
    print('x es menor a 5')
print("Fin del If")

x = 15
y = 20

if x > 10 and y > 25:
    print('X es mayor a 10 y Y mayor a 25')
if x > 10 or y > 25:
    print('X es mayor a 10 o Y mayor a 25')

if not x > 10:
    print('X no es mayor a 10')

is_member = True
age = 15

if is_member:
    if age >= 18:
        print('Puede entrar')
    else:
        print('Eres miembro pero no mayor de edad. No puede entrar')
else:
    print('No es miembro')