from flask import current_app
from flask_restx import Resource
from flask import Flask, render_template, request, redirect, url_for
from src.api.api_def import api, responses
from src.api.models import health_response_model, todos_response_model
from src.db._create_local import Todo
from src.db.session import Session

todo = api.namespace("todo")

@todo.route("/", strict_slashes=False)
@api.doc(responses=responses)
class Endpoints(Resource): 
    """ API Healthcheck class """ 
    @api.response(200, "success", health_response_model)
    @api.marshal_with(todos_response_model)
    def get(self): 
        session = Session()
        todo_list = session.query(Todo).all()
        print("todo list", todo_list)
        return todo_list
        # return render_template("base.html", todo_list = todo_list)

# @todo.route("/")
# def index(self): 
#     return "hello world"


# @app.route("/add", methods=["POST"])
# def add(): 
#     # Add new item 
#     title = request.form.get("title")
#     new_todo = Todo(title=title, complete=False)
#     db.session.add(new_todo)
#     db.session.commit()
#     return redirect(url_for("index"))

# @app.route("/update/<int:todo_id>")
# def update(todo_id): 
#     todo = Todo.query.filter_by(id=todo_id).first()
#     todo.complete = not todo.complete 
#     db.session.commit()
#     return redirect(url_for("index"))

# @app.route("/delete/<int:todo_id>")
# def delete(todo_id): 
#     todo = Todo.query.filter_by(id=todo_id).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect(url_for("index"))
