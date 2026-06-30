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
        
 
@app.get("/students")
def get_student(db:Session = Depends(get_db)):
    return db.query(models.Student).all()

@app.post("/students")
def create_student(name:str, email:str, db:Session = Depends(get_db)):
    new_student = models.Student(name = name, email = email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
    