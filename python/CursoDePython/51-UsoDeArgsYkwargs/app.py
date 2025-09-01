from employee import Employee


# Args
def add_numbers(*args):
    return sum(args)


# Kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Unpacked
def unpacked_add(a, b, c):
    return a + b + c


# Unpacked
def show_info(name, age):
    print(f"Name: {name} Age: {age}")


if __name__ == "__main__":
    # Args
    print(add_numbers(1, 2, 3, 4, 5))
    print(add_numbers(1, 2))
    print(add_numbers(1, 15))
    # Kwargs
    print_info(name="Juan", age=25, city="Saltillo")
    print_info(name="Juan", age=25, city="Saltillo", country="Mexico")

    # Using a class
    employee = Employee("Juan", "Python", "Java", "C++", age=28, city="Saltillo")
    employee.show_employee()

    # Unpacking args
    values = (1, 2, 3)
    print(unpacked_add(*values))

    # Unpacking kwargs
    data = {"name": "Edson", "age": 28}
    show_info(**data)

"""
ToDo: Crea una función que reciba una cantidad de variables de productos y sus precios,
calcule el total y aplique un descuento opcional si se proporciona como un argumento 
con nombre
1. Usar args para recibir una lista de precios.
2. Usar kwargs para aceptar un descuento opcional y aplicarlo al total.
"""
