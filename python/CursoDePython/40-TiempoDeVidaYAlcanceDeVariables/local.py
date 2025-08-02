x = 100


def local_function():
    """
    A simple function that initializes a local variable and prints its value.

    :return: None
    :rtype: NoneType
    """
    x = 10
    print(f"x (local) = {x}")


def global_function():
    """
    Provides a global function that prints the value of a global variable `x`.

    :return: None
    :rtype: None
    """
    print(f"x (global) = {x}")


local_function()
global_function()
print(x)
