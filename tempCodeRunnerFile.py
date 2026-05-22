class Restaurant:
    def __init__(self, restautrant, location, rating):
        self.restaurant = restautrant
        self.location = location
        self.rating = rating

    def info(self):
        print(f"restaurant: {self.restaurant}")
        print(f"location: {self.location}")
        print(f"rating: {self.rating}")

    def str(self):
        return "{} - {} - {}".format(self.restaurant, self.location, self.rating)


rest_1 = Restaurant("alka", "mumbai", "4.0")

print(str(rest_1.info()))