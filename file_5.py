# Class method and static method


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

    @classmethod
    def set_raise_amt(clss, amount):
        clss.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


emp_1 = Employee("corey", "schafer", 50000)
emp_2 = Employee("test", "user", 60000)

emp_str_1 = "john-doe-70000"
emp_str_2 = "steve-smith-30000"
emp_str_3 = "jane-doe-90000"

# first, last, pay = emp_str_1.split("-")

# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fisrt)
print(new_emp_1.pay)


# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# import datetime

# my_date = datetime.date(2016, 7, 11)

# print(Employee.is_workday(my_date))
