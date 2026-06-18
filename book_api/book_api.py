from fastapi import FastAPI

app = FastAPI()

book = [
    {"id":1, "title":"python guide", "author":"corey"},
    {"id":2, "title":"About the life", "author":"mike"}
]

@app.get("/books")
def get_books():
    return book

@app.post("/books")
def post_books(title:str, author:str):
    new_book = {"id":3, "title":title, "author":author}
    book.append(new_book)
    return new_book

@app.delete("/books/{id}")
def del_book(id:int):
    return {"deleted":id}
