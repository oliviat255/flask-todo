from src.db.session import Session, engine
from src.db.models.base import Base 
from src.db.models.todo import Todo

def seed(): 
    """Create data for local database needed for local testing"""
    session = Session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    todo1 = Todo(title="todo 1", complete=False)
    todo2 = Todo(title="todo 2", complete=False)
    session.add_all([todo1, todo2])
    session.commit()
    session.close()
