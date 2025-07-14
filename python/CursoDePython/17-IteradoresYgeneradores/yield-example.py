def ejemplo():
    print("Inicio")
    yield "Primer valor"
    print("Después del primer yield")
    yield "Segundo valor"
    print("Después del segundo yield")
    yield "Tercer valor"

get = ejemplo()
print(next(get))
print(next(get))
print(next(get))
