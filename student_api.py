from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def get_students():
    return {"students": ["sahil", "rahul", "raj"]}
