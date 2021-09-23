from flask_restx import Resource, Namespace, fields

from src.namespace.todo.models import todo_model_def, todo_list_model_def
from src.namespace.todo.service import get_todo_by_id

from src.db.session import Session
from src.db.models.todo import Todo 

todo_ns = Namespace("todo", description="Operations to create, read, update, delete todos")

# Register models to namespace 
todo_model = todo_ns.model("Todo", todo_model_def)
todo_list_model = todo_ns.model("TodoList", todo_list_model_def)

@todo_ns.route("/", strict_slashes=False)
@todo_ns.doc(responses={
    400: "Bad Request", 
    500: "Internal Server Error" 
})
class Todos(Resource): 
    """Todos""" 
    
    @todo_ns.response(200, "Success", todo_list_model)
    @todo_ns.marshal_with(todo_model)
    def get(self):  
        """Get list of all todos"""
        session = Session()
        todo_list = session.query(Todo).all()
        session.close()
        return todo_list
    
    @todo_ns.response(201, "Created", todo_ns.model("TodoId",
    {"todoId": fields.Integer(description="Todo identifier")}))
    def post(self): 
        """Create new todo """
        title = request.form.get("title")
        # todo check if todo already exists 
        new_todo = Todo(title=title, complete=False)
        session = Session()
        session.add(new_todo)
        session.commit()
        return new_todo.id, 201
        

@todo_ns.route("/<int:todo_id>", strict_slashes=False)
@todo_ns.doc(responses={
    400: "Bad Request", 
    404: "TodoId does not exist",
    500: "Internal Server Error" 
})
@todo_ns.param("id", "todo identifer")
class TodoItem(Resource): 
    """ Todo item """

    @todo_ns.response(200, "Success", todo_model)
    @todo_ns.marshal_with(todo_model)
    def get(self, todo_id: int): 
        """Get single todo"""
        return get_todo_by_id(todo_id) 
    
    @todo_ns.response(201, "Created", todo_model)
    @todo_ns.marshal_with(todo_model, 201)
    def put(self, todo_id: int): 
        """Update single todo"""
        todo = get_todo_by_id(todo_id)
        todo.complete = not todo.complete 
        return todo
        
    @todo_ns.response(204, "No Content")
    def delete(self, todo_id: int): 
        """Delete single todo"""
        session = Session()
        todo = session.query(Todo).filter_by(id=todo_id).first()
        session.delete(todo)
        session.commit()
        session.close()
