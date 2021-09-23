"""Model for todo"""
from src.db.models.base import Base
from sqlalchemy import Column, String, Integer, Boolean

class Todo(Base):
    """Class defining a todo object"""
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    complete = Column(Boolean)