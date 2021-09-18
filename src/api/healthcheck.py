from flask import current_app
from flask_restx import Resource
from src.api.api_def import api, responses
from src.api.models import health_response_model

health = api.namespace("health")

@health.route("/api", strict_slashes=False)
@api.doc(responses=responses)
class Healthcheck(Resource): 
    """ API Healthcheck class """ 
    @api.response(200, "success", health_response_model)
    @api.marshal_with(health_response_model)
    def get(self): 
        return{"message": "application healthy"}