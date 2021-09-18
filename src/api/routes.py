from flask import current_app
from flask_restx import Resource
from flask import Flask, render_template, request, redirect, url_for
from src.api.api_def import api, responses
from src.api.models import health_response_model

todo = api.namespace("todo")

# @todo.route("/", strict_slashes=False)
# @api.doc(responses=responses)
# class TodoEndpoints(Resource): 
    
    # @api.response(200, "success", health_response_model)
    # @api.marshal_with(health_response_model)
    # def post(self): 
    #     title = request.form.get('title')
    #     new_todo = Todo(title=title, complete=False)
    #     db.session.add(new_todo)
    #     db.session.commit()
    #     return redirect(url_for("index"))

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
