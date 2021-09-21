from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base  
from src.db.session import Session, engine

Base = declarative_base()

class Todo(Base):
    """ Class defining a todo object """
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    complete = Column(Boolean)

def seed(): 
    session = Session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    todo1 = Todo(title="todo 1", complete=False)
    todo2 = Todo(title="todo 2", complete=False)
    session.add_all([todo1, todo2])
    session.commit()
    session.close()
