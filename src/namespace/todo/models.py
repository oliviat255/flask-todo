from flask_restx import fields, Model
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base  

# todo model 
todo_model_def = Model('Todo', {
    "id": fields.String, 
    "title": fields.String,
    "complete": fields.Boolean
})

# todo list model 
todo_list_model_def = Model("TodoList", {
    "todos": fields.List(fields.Nested(todo_model_def))
})

