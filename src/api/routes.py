""" CRUD on todos """ 
from flask import current_app
from flask_restx import Resource
from flask import Flask, redirect, request, url_for
from src.api.api_def import api, responses
from src.api.models import todos_response_model
from src.db._create_local import Todo
from src.db.session import Session

todo = api.namespace("todo")

@todo.route("/", strict_slashes=False)
@api.doc(responses=responses)
class Todos(Resource): 
    """ Todo endpoint class """ 
    @todo.marshal_with(todos_response_model)
    def get(self):  
        session = Session()
        todo_list = session.query(Todo).all()
        session.close()
        return todo_list
    
    def post(self): 
        title = request.form.get("title")
        new_todo = Todo(title=title, complete=False)
        session = Session()
        session.add(new_todo)
        session.commit()
        # TODO this should not be hard coded 
        return redirect("http://127.0.0.1:5000/")

@todo.route("/<int:todo_id>", strict_slashes=False)
@api.doc(responses=responses)
@todo.param("id", "Todo identifer")
class TodoById(Resource): 
    def put(self, todo_id): 
        session = Session()
        todo = session.query(Todo).filter_by(id=todo_id).first()
        todo.complete = not todo.complete 
        session.commit()
        session.close()
        return True
        # return redirect("http://127.0.0.1:5000/")

# @app.route("/delete/<int:todo_id>")
# def delete(todo_id): 
#     todo = Todo.query.filter_by(id=todo_id).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect(url_for("index"))
