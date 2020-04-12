class Account(object):

    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = opening_balance
        print("Account created for {}.".format(self.name,), end='')
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.00:
            self._balance += amount
            print("{:.2f} Deposited".format(amount / 100))
        return self._balance

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("{:.2f} withdraw".format(amount / 100))
            return amount
        else:
            print("This amount must be grater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    raj = Account("Raj")
    raj.deposit(1010)
    raj.deposit(10)
    raj.deposit(10)
    raj.withdraw(30)
    raj.withdraw(0)
    raj.show_balance()