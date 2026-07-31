def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    while True:
        print("Seleccione la operacion que desea realizar")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        option = int(input("Ingrese la opcion: "))

        if (option == 5):
            print("Gracias por usar el caculator")
            break

        if option < 1 or option > 5:
            print("Opcion invalida")
            continue

        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))

        if option == 1:
            print("La suma es ", add(num1, num2))
        elif option == 2:
            print("La resta es ", substract(num1, num2))
        elif option == 3:
            print("La multiplicacion es ", multiply(num1, num2))
        elif option == 4:
            print("La division es ", divide(num1, num2))

calculator()