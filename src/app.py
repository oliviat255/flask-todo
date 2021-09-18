import os 

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from src.api.api_def import api 

def create_app(environment: str): 
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push() 
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
        blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
        api.init_app(blueprint)
        app.register_blueprint(blueprint)
    except Exception as err: 
        raise err 
