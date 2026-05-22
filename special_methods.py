class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("corey", "schafer", 50000)
emp_2 = Employee("test", "employee", 60000)

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__)

print(int.__add__(1, 2))
print(str.__add__("a", "b"))

print(emp_1 + emp_2)

print(len("test"))
print("test".__len__())
print(len(emp_1))

# problem  1:


class Restaurant:
    def __init__(self, restautrant, location, rating):
        self.restaurant = restautrant
        self.location = location
        self.rating = rating

    def info(self):
        print(f"restaurant: {self.restaurant}")
        print(f"location: {self.location}")
        print(f"rating: {self.rating}")

    def __str__(self):
        return "{} - {} - {}".format(self.restaurant, self.location, self.rating)

    def __repr__(self):
        return "Restaurant('{}','{}','{}')".format(
            self.restaurant, self.location, self.rating
        )

    def __len__(self):
        return len(self.restaurant)

    def __add__(self, other):
        return self.rating + other.rating


rest_1 = Restaurant("alka", "mumbai", 4.0)
rest_2 = Restaurant("dumer", "pune", 3.9)
print(rest_1)
print(repr(rest_1))
print(len(rest_1))
print(rest_1 + rest_2)

# problem solving 2:


class BankAccount:
    def __init__(self, acconut, balance):
        self.account = acconut
        self.balance = balance

    def __str__(self):
        return "{} - {} ".format(self.account, self.balance)

    def __repr__(self):
        return "BankAccount('{}', '{}')".format(self.account, self.balance)

    def __len__(self):
        return len(self.account)

    def __add__(self, other):
        return self.balance + other.balance


acc_1 = BankAccount("sahil", 10000)
acc_2 = BankAccount("tejas", 20000)

print(acc_1)
print(repr(acc_1))
print(len(acc_1))
print(acc_1 + acc_2)


class BankAccount:
    def __init__(self, acconut, balance):
        self.account = acconut
        self.balance = balance

    def __str__(self):
        return "{} - {} ".format(self.account, self.balance)

    def __repr__(self):
        return "BankAccount('{}', '{}')".format(self.account, self.balance)

    def __len__(self):
        return len(self.account)

    def __add__(self, other):
        return self.balance + other.balance


acc_1 = BankAccount("sahil", 10000)
acc_2 = BankAccount("tejas", 20000)

print(acc_1)
print(repr(acc_1))
print(len(acc_1))
print(acc_1 + acc_2)
