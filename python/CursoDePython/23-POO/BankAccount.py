class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.is_active = True
        print(f'Se creó la cuenta de {self.account_holder} con un saldo inicial de {self.balance}')

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. Saldo actual: {self.balance}')
        else:
            print('Cuenta inactiva. No se puede depositar.')

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f'Se ha retirado {amount}. Saldo actual: {self.balance}')

    def deactivate(self):
        self.is_active = False
        print('Cuenta inactivada.')

    def activate(self):
        self.is_active = True
        print('Cuenta activada.')

account1 = BankAccount('Edson', 101010100, 1000)
account2 = BankAccount('Sara', 101010101, 1500)

account1.deposit(50)
account2.deposit(100)

account1.deactivate()
account1.withdraw(50)

account2.withdraw(100)

account1.activate()
account1.withdraw(50)
