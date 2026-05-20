class Animal:
    def __init__(self, name, breed, numbers):
        self.name = name
        self.breed = breed
        self.numbers = numbers


class Birds(Animal):
    def __init__(self, name, numbers):
        self.name = name
        self.number = numbers


species_1 = Animal("mice", "pitbull", "5")
species_2 = Animal("slice", "german", "4")

flying_species_1 = Birds("flamingo", "5")
flying_species_2 = Birds("peacock", "3")
flying_species_3 = Birds("pigeon", "4")


print(species_1.breed)
print(species_1.name)

print(species_2.breed)
print(species_2.name)

print(flying_species_1.name)
print(flying_species_1.number)


class Animal:
    def __init__(self, name, breed, numbers):
        self.name = name
        self.breed = breed
        self.numbers = numbers

    def info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Numbers: {self.numbers}")


class Birds(Animal):
    def __init__(self, name, numbers):
        super().__init__(name, breed="Bird", numbers=numbers)

    def fly(self):
        print(f"{self.name} is flying!")


species_1 = Animal("Mice", "Pitbull", 5)
species_2 = Animal("Slice", "German", 4)

flying_species_1 = Birds("Flamingo", 5)
flying_species_2 = Birds("Peacock", 3)
flying_species_3 = Birds("Pigeon", 4)

# Animal info
species_1.info()
species_2.info()

# Birds info - using parent method!
flying_species_1.info()
flying_species_1.fly()


class Vehicle:
    def __init__(self, name, speed, fuel):
        self.name = name
        self.speed = speed
        self.fuel = fuel

    def info(self):
        print(f"name: {self.name}")
        print(f"speed: {self.speed}")
        print(f"fuel: {self.fuel}")


class ChildCar(Vehicle):

    def __init__(self, name, speed, fuel, doors=4):
        super().__init__(name, speed=speed, fuel=fuel)
        self.doors = doors

    def drive(self):
        print(f"{self.name} is driving")


class ChildBoat(Vehicle):
    def __init__(self, name, speed, fuel, length=10.5):
        super().__init__(name, speed=speed, fuel=fuel)
        self.length = length

    def sail(self):
        print(f"{self.name} is sailing")


model_1 = Vehicle(
    "maruti",
    "150",
    "50L",
)
model_2 = Vehicle(
    "honda",
    "200",
    "30L",
)

toy_model_1 = ChildCar("car800", "100", "10L", doors=4)
toy_model_2 = ChildCar("lex200", "150", "60", doors=6)

sail_boat = ChildBoat("corex100", 150, "200L", length=6.84)

# print(model_1.fuel)
# print(toy_model_1.name)
# print(sail_boat.name)
# print(sail_boat.speed)

# model_1.info()
# model_2.info()

toy_model_1.info()
print(f"doors: {toy_model_1.doors}")
toy_model_1.drive()

toy_model_2.info()
print(f"doors: {toy_model_2.doors}")
toy_model_2.drive()

sail_boat.info()
print(f"length: {sail_boat.length}")
sail_boat.sail()
