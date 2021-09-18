import os 

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

def create_app(environment: str): 
    app = Flask(__name__)
    configure_app(app, environment)
    db = SQLAlchemy(app)
    return app 

def configure_app(app: Flask, environment:str): 
    """
    Applies supplied configuration to the environment
    """
    config_name_map = {
        "development": "config.DevConfig"
    }   
    try: 
        app.config.from_object(config_name_map[environment])
        # TODO - maybe compress here? 
        #  TODO - maybe use blueprint here???
    except Exception as err: 
        raise err 


env = os.environ["FLASK_ENV"]
app = create_app(env)


@app.route("/")
def index(): 
    return "hello world"

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

if __name__ == "__main__": 
    try: 
        app.run(host="0.0.0.0", port=8080)
    except Exception as err: 
        raise err 