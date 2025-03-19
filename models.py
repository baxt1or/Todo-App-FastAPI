from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base

class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())