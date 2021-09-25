from typing import Optional
from werkzeug.exceptions import NotFound
from src.db.session import Session
from src.db.models.todo import Todo 

def get_todo_by_id(todo_id: int) -> Todo: 
    """Get todo details by id"""
    session = Session() 
    todo = session.query(Todo).filter_by(id=todo_id).first()
    if not todo: 
        raise NotFound("404 - Todo not found")
    return todo 

def get_todo_by_name(todo_name: Optional[str]) -> Optional[Todo]: 
    """Get todo details by name"""
    session = Session()
    todo = session.query(Todo).filter_by(title=todo_name).first()
    if not todo: 
        return None
    return todo 
