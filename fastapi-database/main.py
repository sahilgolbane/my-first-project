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
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@app.get("/students/{id}")
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students")
def create_student(name: str, email: str, db: Session = Depends(get_db)):
    new_student = models.Student(name=name, email=email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.put("/students/{id}")
def update_student(id: int, name: str, email: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = name
    student.email = email
    db.commit()
    return student

@app.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted"}
