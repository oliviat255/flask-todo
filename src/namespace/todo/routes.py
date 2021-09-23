from flask import current_app
from flask import Flask, redirect, request, url_for

from flask_restx import Resource, Namespace, fields

from src.namespace.todo.models import todo_model_def
from src.namespace.todo.service import get_todo_by_id
from src.db._create_local import Todo
from src.db.session import Session

todo_ns = Namespace("todo", description="Operations to create, read, update, delete todos")

# Register models to namespace 
todo_model = todo_ns.model("Todo", todo_model_def)


@todo_ns.route("/", strict_slashes=False)
@todo_ns.doc(responses={
    400: "Bad Request", 
    500: "Internal Server Error" 
})
class Todos(Resource): 
    """ Todos  """ 
    
    def get(self):  
        """ Get all todos """
        session = Session()
        todo_list = session.query(Todo).all()
        session.close()
        return todo_list
    
    @todo_ns.response(201, "Created", todo_ns.model("TodoId",
    {"todoId": fields.Integer(description="Todo identifier")}))
    def post(self): 
        """ Create new todo """
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

    @todo_ns.response(201, "Created", todo_model)
    def put(self, todo_id): 
        """ Update single todo """
        todo = get_todo_by_id(todo_id)
        todo.complete = not todo.complete 
        return todo 
        
    
    def delete(self, todo_id): 
        """ Delete single todo """
        session = Session()
        todo = session.query(Todo).filter_by(id=todo_id).first()
        session.delete(todo)
        session.commit()
        session.close()

# @app.route("/delete/<int:todo_id>")
# def delete(todo_id): 
#     todo = Todo.query.filter_by(id=todo_id).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect(url_for("index"))
