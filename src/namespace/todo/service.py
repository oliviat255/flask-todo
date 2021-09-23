from src.db.session import Session
from src.namespace.todo.models import Todo 

def get_todo_by_id(todo_id: int) -> Todo: 
    """Get todo details by id"""
    session = Session() 
    todo = session.query(Todo).filter_by(id=todo_id).first()
    return todo 