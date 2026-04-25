# practice

# CLASSMETHOD AND STATICMETHOD


class circle:

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


circle_1 = circle(5)
print(f" circle 1 radius: {circle_1.radius}")

circle_2 = circle.from_diameter(20)
print(f" circle 2 radius : {circle_2.radius}")


practice: 2


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(clss, string):
        name, salary = string.split("-")
        return clss(name, salary)


new_emp_1 = Employee.from_string("sahil-50000")
new_emp_2 = Employee.from_string("tejas-40000")
print(new_emp_1.name)
print(new_emp_1.salary)

print(new_emp_2.name)
print(new_emp_2.salary)


practice: 3


class temperature:

    @staticmethod
    def is_celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9


print(temperature.is_celsius_to_fahrenheit(100))
print(temperature.fahrenheit_to_celsius(212))

practice: 4

""" COMBINED PRACTICE"""


class Product:

    def __init__(self, product, price):
        self.product = product
        self.price = price

    @staticmethod
    def is_affordable(price):
        if price < 1000:
            return True

    @classmethod
    def from_string(clss, string):
        product, price = string.split("-")
        return clss(product, price)


new_item_1 = Product.from_string("chips-50")
new_item_2 = Product.from_string("chocolate-100")


print(Product.is_affordable(900))
print(new_item_1.product)
print(new_item_1.price)

print(new_item_2.product)
print(new_item_2.price)
