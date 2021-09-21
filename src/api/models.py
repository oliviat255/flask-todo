from flask_restx import fields 
from src.api.api_def import api 
from sqlalchemy import Column, String, Integer, Boolean

health_response_model = api.model("HealthResponse", {
    "message": fields.String(description="Healthcheck response")
})


