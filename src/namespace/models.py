from flask_restx import fields, Model
from src.api.api_def import api 


# TODOS RESPONSE MODEL 
todos_response_model = Model('TodosResponse', {
    "id": fields.String, 
    "title": fields.String,
    "complete": fields.Boolean
})