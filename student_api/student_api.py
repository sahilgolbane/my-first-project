from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Sahil", "grade": "A"},
    {"id": 2, "name": "Tejas", "grade": "B"}
]

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def post_students(name: str, grade: str):
    new_student = {"id": 3, "name": name, "grade": grade}
    students.append(new_student)
    return new_student

@app.delete("/students/{id}")
def del_students(id: int):
    return {"deleted": id}
