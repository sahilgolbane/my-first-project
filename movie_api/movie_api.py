from fastapi import FastAPI

app = FastAPI()

movies = [
    {"id":1, "title":"commando", "title":2010},
    {"id":2, "title":"games of thrones", "year":2014}
]


@app.get("/movies")
def get_movies():
    return movies

@app.post("/movies")
def post_movies(title:str, year:int):
    new_movie = {"id":3, "title":title, "year":year}
    movies.append(new_movie)
    return new_movie

@app.delete("/movies/{id}")
def del_movies(id:int):
    return {"deleted":id}
