def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_(n):
    if n == 0:
        return 1
    else:
        return n * factorial_(n - 1)

factorial_5 = factorial_(5)
print(factorial_5)

print(factorial(5))

# Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = 0
print(fibonacci(number))