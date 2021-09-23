"""Model for todo"""
from sqlalchemy import Boolean, Column, Integer, String
from src.db.models.base import Base

class Todo(Base):
    """Class defining a todo object"""
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    complete = Column(Boolean)