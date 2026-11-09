class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money):
        self.balance += money

a = BankAccount("Іван", 1000)
a.deposit(500)
print(a.name, a.balance)
