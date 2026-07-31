import statistics, csv

monthly_sales = {}
with open('monthly_sales.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        month = row['month']
        sales = float(row['sales'])
        monthly_sales[month] = sales

print(f'monthly sales: {monthly_sales}')
sales = list(monthly_sales.values())        # Only values
print(sales)

# Media (Promedio)
mean_sales = statistics.mean(sales)
print(f'Media: {mean_sales}')

# Mediana
median_sales = statistics.median(sales)
print(f'Mediana: {median_sales}')

# Moda
mode_sales = statistics.mode(sales)
print(f'Moda: {mode_sales}')

# Desviación estándar
stdev_sales = statistics.stdev(sales)
print(f'La desviación estándar es: {stdev_sales}')

# Hallar la varianza
variance_sales = statistics.variance(sales)
print(f'La varianza es: {variance_sales}')

# Maximo
max_sales = max(sales)
print(f'Maximo: {max_sales}')

# Mínimo
min_sales = min(sales)
print(f'Minimo: {min_sales}')

range_sales = max_sales - min_sales
print(f'Rango: {range_sales}')
