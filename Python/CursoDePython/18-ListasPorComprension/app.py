squares = [x**2 for x in range(1, 11)]
print("Los cuadrados son: ", squares)

# Conversión de grados Celsius a Fahrenheit
celsius = [0, 10, 20.1, 34.5]
fahrenheit = [temp * 9 / 5 + 32 for temp in celsius]
print("Los grados Fahrenheit son: ", fahrenheit)

# Números pares
evens = [x for x in range(1, 21) if x%2 ==0]
print(evens)

"""
Ejercicios:
Doble de los Números
Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.

Filtrar y Transformar en un Solo Paso
Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

Crear un Diccionario con List Comprehension
Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.

Anidación de List Comprehensions
Dada una lista de listas (una matriz):

pythonCopiar código
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Calcula la matriz traspuesta utilizando una List Comprehension anidada.

Extraer Información de una Lista de Diccionarios
Dada una lista de diccionarios que representan personas:

pythonCopiar código
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

List Comprehension con un else
Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.
"""