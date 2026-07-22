from pydantic import BaseModel


class TaskCreate(BaseModel):
    title:str
    done:bool
    priority:int


class TaskUpdate(BaseModel):
    title:str
    done:bool
    priority:int