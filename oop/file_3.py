# OOP
# CLASS VARIABLE

# THE CODE IS WRITTEN FOR UNDERSTANDING/COPYING THE CONCEPT/EACH LINE OF CODE AND DEEP LEARNING IT.


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.fisrt = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.fisrt, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("corey", "schafer", 50000)
emp_2 = Employee("test", "user", 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.__dict__)

emp_1.raise_amount = 1.05

print(Employee.num_of_emps)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
