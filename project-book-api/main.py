from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

@app.get("/books")
def get_book(db:Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.post("/books")
def create_Book(title:str, author:str, year:int, db:Session = Depends(get_db)):
    new_Book = models.Book(title = title, author = author, year = year)
    db.add(new_Book)
    db.commit()
    db.refresh(new_Book)
    return new_Book

@app.get("/books/{id}")
def get_Book(id:int, db:Session = Depends(get_db)):
    Book = db.query(models.Book).filter(models.Book.id == id).first()
    if not Book:
        raise HTTPException(status_code=404, detail="Book not found")
    return Book

@app.put("/books/{id}")
def update_Book(id:int,title:str, author:str, year:int, db:Session = Depends(get_db)):
    Book = db.query(models.Book).filter(models.Book.id == id).first()
    if not Book:
        raise HTTPException(status_code=404, detail="Book not found")
    Book.title = title
    Book.author = author
    Book.year = year
    db.commit()
    return Book

@app.delete("/books/{id}")
def get_delete(id:int, db:Session = Depends(get_db)):
    Book = db.query(models.Book).filter(models.Book.id == id).first()
    if not Book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(Book)
    db.commit()
    return {"message":"Book deleted"}
