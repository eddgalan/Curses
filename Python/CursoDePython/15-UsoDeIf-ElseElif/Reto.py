playerSelection1 = input("Ingrese Piedra, Papel o Tijera: ").lower()
playerSelection2 = input("Ingrese Piedra, Papel o Tijera: ").lower()

options = ("piedra", "papel", "tijera")

if playerSelection1 not in options:
    print("El jugador 1 ingresó una opción NO válida")
if playerSelection2 not in options:
    print("El jugador 2 ingresó una opción NO válida")

if playerSelection1 == playerSelection2:
    print("Empate")
elif playerSelection1 == "piedra" and playerSelection2 == "tijera" or \
        playerSelection1 == "papel" and playerSelection2 == "piedra" or \
        playerSelection1 == "tijera" and playerSelection2 == "papel":
    print("El jugador 1 gana")
elif playerSelection1 == "tijera" and playerSelection2 == "piedra" or \
        playerSelection1 == "papel" and playerSelection2 == "tijera" or \
        playerSelection1 == "piedra" and playerSelection2 == "papel":
    print("El jugador 2 gana")
