import os, math, random

# OS Library
cwd = os.getcwd()
print(f'Current Working Directory: {cwd}')

# Listar archivos
all_files = [f for f in os.listdir('.')]
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

print('All Files: ', all_files)
print('txt Files: ', txt_files)

# Renombrar archivo
try:
    os.rename('txt_file1.txt', 'txt_file1_renamed.txt')
    print('Renamed txt_file1.txt to txt_file1_renamed.txt')
except FileNotFoundError:
    print('Error: File "txt_file1.txt" not found')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print('txt Files: ', txt_files)

#Math Library
# Hallar el área y perímetro de un círculo
radius = 5
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
print(f'Area: {area}')
print(f'Perimeter: {perimeter}')


#Random Library
# Generar un número entero aleatorio
random_number = random.randint(1, 10)
print(f'Random Number: {random_number}')

# Colores aleatorios
colors = ['red', 'green', 'blue', 'yellow', 'orange']
random_color = random.choice(colors)
print(f'Random Color: {random_color}')

# Barajar lista de cartas
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cards)
print(f'Cards: {cards}')
