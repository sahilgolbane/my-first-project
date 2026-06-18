from fastapi import FastAPI

app = FastAPI()

todos = [ 
    {"id":1,"task":"learn python"},
    {"id":2,"task":"learn fastapi"}
]

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def post_todos(task: str):
    new_todo = {"id":3, "task": task}
    todos.append(new_todo)
    return new_todo

@app.delete("/todos/{id}")
def del_todos(id:int):
    return {"deleted":id}
