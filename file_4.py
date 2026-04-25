# CLASS VARIABLES PROBLEMS PRACTICE


class Gym_member:

    num_of_memb = 0
    cancel_of_memb = 0

    def __init__(self, member, number):
        self.member = member
        self.number = number

        Gym_member.num_of_memb += 1

    def cancel_membership(self):
        Gym_member.cancel_of_memb += 1
        return Gym_member.num_of_memb - Gym_member.cancel_of_memb


person_1 = Gym_member("sahil", "one")
person_2 = Gym_member("tejas", "two")
person_3 = Gym_member("onmkar", "three")

print(f"Total members: {Gym_member.num_of_memb}")

person_1.cancel_membership()

Total = Gym_member.num_of_memb - Gym_member.cancel_of_memb

print(f" After cancellation: {Total}")

pratice: 2


class library:

    total_books = 0
    num_of_newbook = 0

    def __init__(self, newbook, numbers):
        self.newbook = newbook
        self.numbers = numbers

        library.num_of_newbook += 1

    def remove_book(self):
        library.num_of_newbook -= 1

    def show_total(self):
        print(f"Total books: {library.num_of_newbook}")


person_1 = library("history", "one")
person_2 = library("maths", "two")
person_3 = library("science", "three")
person_4 = library("classmate", "four")
person_5 = library("english", "five")

print(person_1.newbook)
print(person_4.newbook)
print(person_4.numbers)

person_1.show_total()

person_1.remove_book()
person_3.remove_book()

person_4.show_total()

# practice:3


class storeitem:
    discount_rate = 0.10

    def __init__(self, product, price):
        self.product = product
        self.price = price

    def get_final_price(self):
        return self.price - (self.price * storeitem.discount_rate)


product_1 = storeitem("haircream", 5000)
product_2 = storeitem("shampoo", 6000)
product_3 = storeitem("soap", 3000)

print("Before discount change:")
print(f"{product_1.product}: {product_1.get_final_price()}")
print(f"{product_2.product}: {product_2.get_final_price()}")
print(f"{product_3.product}: {product_3.get_final_price()}")

storeitem.discount_rate = 0.20

print("\nAfter discount change:")
print(f"{product_1.product}: {product_1.get_final_price()}")
print(f"{product_2.product}: {product_2.get_final_price()}")
print(f"{product_3.product}: {product_3.get_final_price()}")


class Developer:
    bonus = 500  # Class Variable


dev1 = Developer()
dev2 = Developer()

dev1.bonus = 700  # Changing via instance

print(dev1.bonus)
print(dev2.bonus)
print(Developer.bonus)
