from pydantic import BaseModel


class TaskCreate(BaseModel):
    title:str
    done:bool
    priority:int
    user_id:int


class TaskUpdate(BaseModel):
    title:str
    done:bool
    priority:int
    

class UserCreate(BaseModel):
    name:str
    email:str
