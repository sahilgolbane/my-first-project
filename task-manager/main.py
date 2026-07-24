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
    new_task = models.Task (title=task.title, done=task.done, priority=task.priority, user_id=task.user_id)
    db.add(new_task)
    db.commit() 
    db.refresh(new_task) 
    return new_task

@app.get("/tasks")
def get_tasks(db:Session = Depends(get_db)):
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
    db_task.title = task.title
    db_task.done = task.done
    db_task.priority = task.priority
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

@app.post("/users")
def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    new_user =  models.User (name= user.name, email= user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/users")
def get_users(db:Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get("/users/{id}")
def get_user(id:int, db:Session = Depends(get_db)):
    user =  db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user

@app.get("/users/{id}/tasks")
def get_user_tasks(id:int, db:Session = Depends(get_db)):
    return db.query(models.Task).filter(models.Task.user_id == id).all()       
        




    


