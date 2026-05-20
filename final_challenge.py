#   Create Parent class Restaurant
# 1. Has restaurant_name, location, rating
# 2. Has method info() - prints all details

# Create Child class FastFood that inherits Restaurant
# 1. Has extra attribute delivery_time and min_order
# 2. Has method order() - prints
#    "Ordering from restaurant_name
#     delivery in delivery_time minutes"

# Create Child class FineDiging that inherits Restaurant
# 1. Has extra attribute dress_code and reservation
# 2. Has method book_table() - prints
#    "Table booked at restaurant_name
#     dress code is dress_code"

# Test everything!


class Restaurant:
    def __init__(self, restaurant_name, location, rating):
        self.restaurant = restaurant_name
        self.location = location
        self.rating = rating

    def detail(self):
        print(f"restaurant name: {self.restaurant}")
        print(f"location: {self.location}")
        print(f"rating: {self.rating}")


class FastFood(Restaurant):
    def __init__(
        self, restaurant_name, location, rating, delivery_time=10, min_order=300
    ):
        super().__init__(restaurant_name, location, rating)
        self.deliverytime = delivery_time
        self.minorder = min_order

    def order(self):
        print(f"ordering from: {self.restaurant}")
        print(f"delivery in: {self.minorder} minutes")


class FineDine(Restaurant):
    def __init__(
        self,
        restaurant_name,
        location,
        rating,
        dresscode="white",
        reservation="9am to 1am 5pm to 7pm ",
    ):
        super().__init__(restaurant_name, location, rating)
        self.dresscode = dresscode
        self.reservation = reservation

    def book_table(self):
        print(f"table book at: {self.restaurant}")
        print(f"dresscode is: {self.dresscode}")


Restaurant_1 = Restaurant("alka", "mumbai", "4.0")
Restaurant_2 = Restaurant("dumer", "mountroad", "3.9")

FastFood_1 = FastFood("suber", "westroad", "4.0", "30min", "500")
FastFood_2 = FastFood("aven", "cufftown", "4.9", "1hrs", "600")

finedine_1 = FineDine("alo", "upperwest", "4.0", "blue", "10m to 1pm")
finedine_2 = FineDine("sulet", "lowerwest", "3.9", "orange", "10am to 3pm")

Restaurant_1.detail()

Restaurant_2.detail()

FastFood_1.detail()
print(f"min order: {FastFood_1.minorder}")
print(f"delivery in: {FastFood_1.deliverytime}")


FastFood_2.detail()
print(f"minorder: {FastFood_1.minorder}")
print(f"delivery in: {FastFood_1.deliverytime}")


finedine_1.detail()
print(f"tablebook at: {finedine_1.restaurant}")
print(f"dresscode: {finedine_1.dresscode}")


finedine_2.detail()
print(f"table book at: {finedine_2.restaurant}")
print(f"dresscode: {finedine_2.dresscode}")
