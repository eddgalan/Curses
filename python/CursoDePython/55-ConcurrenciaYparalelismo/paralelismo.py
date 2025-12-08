import multiprocessing

def calculate_square(number):
    return number ** 2

if __name__ == "__main__":
    numbers = range(6)
    #Craete pool
    with multiprocessing.Pool(processes=2) as pool:
        result = pool.map(calculate_square, numbers)

    print(f'Result: {result}')