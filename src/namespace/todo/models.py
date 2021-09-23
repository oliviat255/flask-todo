from flask_restx import fields, Model

# todo model 
todo_model_def = Model('TodosResponse', {
    "id": fields.String, 
    "title": fields.String,
    "complete": fields.Boolean
})