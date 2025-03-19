from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateTodo(BaseModel):
    title : str 
    content : str
    completed : Optional[bool] = False


class Todo(BaseModel):
    id : int
    title : str
    content : str 
    completed : bool
    created_at : datetime


class TodoUpdate(BaseModel):
    title : Optional[str]
    content: Optional[str]
    completed : Optional[bool]