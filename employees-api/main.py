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


@app.get("/employees/count")
def count_employees(db: Session = Depends(get_db)):
    return {"total": db.query(models.Employees).count()}

@app.get("/employees")
def get_employees(department:str=None, sort:str=None, db:Session = Depends(get_db)):
    query = db.query(models.Employees)

    if department:
        query = query.filter(models.Employees.department == department)

    if sort == "salary":
        query = query.order_by(models.Employees.salary) 

    return query.all()

@app.post("/employees")
def create_Employees( name:str, department:str, salary:int, db:Session = Depends(get_db)):
    new_employees = models.Employees(name=name, department=department, salary=salary)
    db.add(new_employees)
    db.commit()
    db.refresh(new_employees)
    return new_employees

@app.get("/employees/{id}")
def get_Employees(id:int, db:Session = Depends(get_db)):
    employees = db.query(models.Employees).filter(models.Employees.id == id).first()
    if not employees:
        raise HTTPException(status_code=404, detail="Employees not found")
    return employees

@app.put("/employees/{id}")
def update_Employees(id:int, name:str, department:str, salary:int, db:Session = Depends(get_db)):
    employees = db.query(models.Employees).filter(models.Employees.id == id).first()
    if not employees:
        raise HTTPException(status_code=404, detail="Employess not found")
    employees.name = name
    employees.department = department
    employees.salary = salary 
    db.commit()
    return employees

@app.delete("/employees/{id}")
def get_delete(id:int, db:Session = Depends(get_db)):
    employees = db.query(models.Employees).filter(models.Employees.id == id).first()
    if not employees:
        raise HTTPException(status_code=404, detail="Employess not found")
    db.delete(employees)
    db.commit()
    return {"message":"Employees deleted"}

     


                     

     

