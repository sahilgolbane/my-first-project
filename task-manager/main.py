from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas        
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks")
def create_task(task: schemas.TaskCreate, db:Session = Depends(get_db)):
    new_task = models.Task (title=task.title, done=task.done, priority=task.priority)
    db.add(new_task)
    db.commit() 
    db.refresh(new_task) 
    return new_task

@app.get("/tasks")
def get_task(db:Session = Depends(get_db)):
    return db.query(models.Task).all()

@app.get("/tasks/{id}")
def get_task(id:int, db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id ==id).first()
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    return task

@app.put("/tasks/{id}")
def update_task(id:int, task: schemas.TaskUpdate, db:Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="task not found")
    db_task = task.title
    db_done = task.done
    db_priority = task.priority
    db.commit()
    return db_task

@app.delete("/tasks/{id}")
def get_delete(id:int, db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id==id).first()
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    db.delete(task)
    db.commit()
    return {"message":"task deleted"}
    


