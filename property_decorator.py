class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return "{} {} ".format(self.first, self.last)

    @property
    def email(self):
        return "{} {}@email.com ".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(
        self,
    ):
        print("Delete Name!")
        self.first = None
        self.last = None


emp1 = Employee("john", "smith")


emp1.first = "jim"

emp1.fullname = "corey schafer"


print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp1 = Person("sahil", "golbane")

emp1.fullname = "ander xaver"

print(emp1.fullname)
print(emp1.fullname)

del emp1.fullname


class BankAccount:
    def __init__(self, owner, _balance):
        self.owner = owner
        self._balance = _balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self):
        if self.balance < 0:
            print("Invalid Amount")
        else:
            print(f"show balance amount: {self.balance}")

    @balance.deleter
    def balance(self):
        print("Account Closed!")
        self.balance = None


acc1 = BankAccount("omkar", 10000)
print(acc1.balance)
acc1._balance = 5000


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid Amount!")
        else:
            self._balance = amount

    @balance.deleter
    def balance(self):
        print("Account Closed!")
        self._balance = 0


acc1 = BankAccount("Sahil", 10000)
print(acc1.balance)
acc1.balance = 5000
print(acc1.balance)
acc1.balance = -1000
del acc1.balance
print(acc1.balance)


class Student:
    def __init__(self,name,_grade):
        self.name = name
        self.grade = _grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,marks):
        if marks < 0:
            print("Invalid marks!")
        elif marks > 100:
            print("Invalid marks!")
        else:
            self._grade = marks

    @grade.deleter
    def grade(self):
        print("Grade removed!")
        self.grade = 0

class1 = Student("sahil",80)
print(class1.name)   
print(class1.grade)

class1.grade = 90
print(class1.grade)
         
class1.grade = 150
print(class1.grade)

del class1.grade
print(class1.grade)


    

        