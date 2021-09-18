from flask_restx import fields 
from src.api.api_def import api 
import flask_sqlalchemy

health_response_model = api.model("HealthResponse", {
    "message": fields.String(description="Healthcheck response")
})

db = flask_sqlalchemy.SQLAlchemy()

class Todo(db.Model):
    """ Class defining a todo object """
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("name", db.String(100))
    complete = db.Column("complete", db.Boolean)