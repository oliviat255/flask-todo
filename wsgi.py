import os 
import requests 
from flask import url_for, render_template
from src.app import create_app

env = os.environ["FLASK_ENV"]
app = create_app(env)

# TODO - add logging here 


@app.route("/")
def index(): 
    url = url_for("api.todo_todos")
    response = requests.get("http://127.0.0.1:5000/api/v1/todos", timeout=5)
    return render_template("index.html", todo_list=response.json())

if __name__ == "__main__":
    try: 
        app.run(host="0.0.0.0", port=8080)
    except Exception as err: 
        raise err 