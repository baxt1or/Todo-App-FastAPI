from fastapi import FastAPI
from database import Base, engine
from routes import router

app = FastAPI(__name__='my_first_todo_app')
app.include_router(router=router)


Base.metadata.create_all(engine)

