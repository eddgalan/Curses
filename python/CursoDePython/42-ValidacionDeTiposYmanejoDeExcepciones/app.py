from typing import Optional


def divide(a: int, b: int) -> Optional[float]:
    # Validación de tipado
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los valores deben ser enteros")
    # Verificar que el divisor no sea cero
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


try:
    result_1 = divide(10, "2")
    print(result_1)
except TypeError as e:
    print(f"Error: {e}")

try:
    result_2 = divide(10, 0)
    print(result_2)
except ValueError as e:
    print(f"Error: {e}")

try:
    result_3 = divide(10, 2)
    print(result_3)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
