# Create Parent class Phone
# 1. Has brand, model, price
# 2. Has method call() - prints "Calling!"

# Create Child class Smartphone that inherits Phone
# 1. Has extra attribute storage (default 128GB)
# 2. Has method app() - prints "Opening app!"

# Test:
# - Create 2 smartphones
# - Print their details
# - Call both methods


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def info(self):
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"price: {self.price}")

    def call(self):
        print(f"brand:{self.brand} is calling!")


class Smartphone(Phone):
    def __init__(self, brand, model, price, storage=128):
        super().__init__(
            brand,
            model,
            price,
        )
        self.storage = storage

    def Methodapp(self):
        print(f"brand: {self.brand} is opening app!")


phone_1 = Phone("samsung", "s18", "34000")
phone_2 = Phone("redmi", "A3", "20000")

variant_1 = Smartphone("apple", "14", "55000", "150")
variant_2 = Smartphone("vivo", "v15", "15000", "128")

phone_1.info()
phone_1.call()
phone_2.info()
phone_2.call()

variant_1.info()
print(f"storage: {variant_1.storage}")
variant_1.Methodapp()
variant_2.info()
print(f"storage: {variant_2.storage}")
variant_2.Methodapp()
