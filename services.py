from models import Todos 
from sqlalchemy.orm import Session

def create_one(title:str, content:str, db:Session):
    
    try:
        new_todo = Todos(title=title, content=content)

        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)

        print("Success")
        return new_todo
    except Exception as e:
        db.rollback()
        print("Failed to create todo", e)
        raise


def get_many(db:Session):
    return db.query(Todos).order_by(Todos.completed,Todos.created_at.desc()).all()

def get_one(id:int, db:Session):

    todo = db.query(Todos).filter(Todos.id == id).first()

    return todo

def delete_one(id:int, db:Session):
    
    todo = get_one(id=id, db=db)

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return todo

    