from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 20000}
]

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def post_products(name: str, price: int):
    new_product = {"id": 3, "name": name, "price": price}
    products.append(new_product)
    return new_product

@app.delete("/products/{id}")
def del_products(id: int):
    return {"deleted": id}
