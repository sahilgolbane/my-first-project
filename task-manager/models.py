from sqlalchemy import Column, Integer, String, Boolean, ForeignKey 
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    done = Column(Boolean)
    priority = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
