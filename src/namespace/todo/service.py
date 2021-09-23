from src.db.session import Session
from src.db._create_local import Todo 
from src.namespace.todo.models import todo_model_def

def get_todo_by_id(todo_id: int): 
    """Get todo details by id"""
    session = Session() 
    todo = session.query(Todo).filter_by(id=todo_id).first()
    return todo 