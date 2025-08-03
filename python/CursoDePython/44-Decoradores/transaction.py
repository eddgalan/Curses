def log_transaction(func):
    def wrapper():
        print("Starting transaction...")
        func()
        print("Finishing transaction...")

    return wrapper


@log_transaction
def process_payment():
    print("Processing payment...")


process_payment()
