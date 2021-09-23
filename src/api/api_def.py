from flask_restx import Api 
from src.api.routes import todo_ns

api = Api(version='1.0', title='Todo Application', 
    description = "Todo application for learning how to build flask applications from scratch", 
    catch_all_404s = True
    )
api.add_namespace(todo_ns, path="/todos")

