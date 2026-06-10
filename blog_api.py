from fastapi import FastAPI

app = FastAPI()

@app.get("/blog")
def  get_blog():
    return {"message": "hello world"}
