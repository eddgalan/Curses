from base_class import BaseClass

if __name__ == "__main__":
    base = BaseClass()
    # Protected
    print(base._attr_protected)
    base._protected_method()
    # Privated
    base.public_method()
    try:
        print(base.__attr_private)  # Error AttributeError
    except AttributeError:
        print("Error: Cannot access private attribute")

"""
ToDo: Implementar una clase CuentaBancaria con un método protegido para actualizar
el saldo de la cuenta. y un método privado para registrar las transacciones internamente.
1. El método protegido (_actualizar_saldo) solo debe ser utilizado dentro de la clase y sus
subclases.
2. El método privado (__registrar_transaccion) debe ser completamente interno y no accesible
fuera de la clase. 
"""