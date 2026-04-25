# practice 2 - basic class


class bankprofile:

    def __init__(self, name, surname, salary, loan):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.loan = loan

    def fullname(self):
        return "{} {}".format(self.name, self.surname)


person_a = bankprofile("rahul", "kumar", "50000", "400000")
person_b = bankprofile("stefen", "roy", "40000", "300000")
person_c = bankprofile("aditya", "pandey", "20000", "100000")

print(person_a.name)
print(person_a.loan)

print(person_b.name)
print(person_b.salary)

print(person_c.salary)
print(person_c.surname)

print("{} {}".format(person_a.name, person_a.surname))


print(person_a.fullname())  # This is by self instance method.

print(bankprofile.fullname(person_c))  # This is by class method.
