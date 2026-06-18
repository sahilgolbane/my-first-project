from fastapi import FastAPI

app = FastAPI()

user = [
    {"id":1, "name":"sahil", "email":"sahil@email.com"},
    {"id":2, "name":"tejas", "email":"tejas@email.com"}
]

@app.get("/users")
def get_user():
    return user

@app.post("/users")
def post_user(name: str, email: str):
    new_user = {"id":3, "name":name, "email":email}
    user.append(new_user)
    return new_user

@app.delete("/users/{id}")
def del_user(id:int):
    return {"deleted":id}
