from collections import Counter


def count_sales(products: list[str]) -> Counter:
    return Counter(products)

sales = [
    'apple',
    'apple',
    'banana',
    'banana',
    'banana',
    'orange',
    'orange',
    'mango',
    'mango',
]
result = count_sales(sales)
print(result)