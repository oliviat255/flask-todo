import os 

from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from src.api.api_def import api 

def create_app(environment: str): 
    app = Flask(__name__)
    configure_app(app, environment)
    return app 

def configure_app(app: Flask, environment:str): 
    """
    Applies supplied configuration to the environment
    """
    config_name_map = {
        "development": "src.config.DevConfig"
    }   
    try: 
        app.config.from_object(config_name_map[environment])
        # TODO - maybe compress here? 
        blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
        api.init_app(blueprint)
        app.register_blueprint(blueprint)
    except Exception as err: 
        raise err 

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     complete = db.Column(db.Boolean)

# @app.route("/")
# def index(): 
#     # show all todos 
#     todo_list = Todo.query.all()
#     return render_template('base.html', todo_list=todo_list)

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
