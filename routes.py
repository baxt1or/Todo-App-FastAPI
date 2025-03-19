from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas import CreateTodo, Todo, TodoUpdate
from services import create_one, get_many, get_one, delete_one
from starlette import status
from typing import List

router = APIRouter(prefix='/todo')


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: CreateTodo, db:Session = Depends(get_db)):
    
    new_todo = create_one(title=todo.title, content=todo.title, db=db)

    return {"message":f"{new_todo.title} Successfully created"}


@router.get("/",response_model=List[Todo])
async def get_todos(db:Session = Depends(get_db)):

    todos = get_many(db=db)

    if todos:
        return todos
    return []

@router.get("/{id}", response_model=Todo)
async def get_todo(id:int, db:Session = Depends(get_db)):

    todo = get_one(id=id, db=db)

    if todo:
        return todo
    return None

@router.delete("/{id}")
async def delete_todo(id:int, db:Session = Depends(get_db)):

    todo = delete_one(id=id, db=db)

    if not todo:
        raise HTTPException(status_code=404, detail="Failed to Delete")
    return {"message":f"{todo.title} Deleted"}

@router.patch("/{id}", response_model=dict)
async def update_todo(id:int, update_todo:TodoUpdate, db:Session = Depends(get_db)):

    updated_todo = get_one(id=id, db=db)

    if not updated_todo:
        raise HTTPException(status_code=404, detail="Failed to find todo")
    
    for field, value in update_todo.dict(exclude_unset=True).items():
        setattr(updated_todo, field, value)
    
    db.commit()
    db.refresh(updated_todo)
    return {"message":f"Todo {id} successfully updated"}