# BankAccount — owner, balance
# - deposit(amount)
# - withdraw(amount)
# - show_balance()

# SavingsAccount inherits BankAccount
# - interest_rate = 0.05
# - add_interest()

# CurrentAccount inherits BankAccount
# - overdraft_limit = 10000
# - check_overdraft()


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit=10000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self):
        available = self.balance + self.overdraft_limit
        print(f"Total available with overdraft: {available}")


# Test parent first
acc_1 = BankAccount("Sahil", 10000)
acc_1.show_balance()
acc_1.deposit(5000)
acc_1.withdraw(3000)
acc_1.show_balance()

savings_1 = SavingsAccount("Sahil", 10000)
savings_1.show_balance()
savings_1.deposit(5000)
savings_1.add_interest()
savings_1.show_balance()

current_1 = CurrentAccount("Tejas", 5000)
current_1.show_balance()
current_1.deposit(3000)
current_1.withdraw(2000)
current_1.check_overdraft()
