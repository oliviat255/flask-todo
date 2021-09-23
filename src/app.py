from flask import Flask, Blueprint
from flask_restx import Api 

from src.api.health.route import health_ns
from src.api.todo.routes import todo_ns
from src.db import _create_local

# define API 
api = Api(version='1.0', title='Todo Application', 
    description = "Todo application for learning how to build flask applications from scratch", 
    catch_all_404s = True
    )

# Add namespaces to api 
api.add_namespace(todo_ns, path="/todos")
api.add_namespace(health_ns, "/health")


def create_app(environment: str): 
    """Create and configure flask application"""
    app = Flask(__name__)
    configure_app(app, environment)
    return app 

def configure_app(app: Flask, environment:str): 
    """Applies supplied configuration to the environmet"""
    config_name_map = {
        "development": "src.config.DevConfig",
        "testing": "src.config.TestConfig"
    }   
    try: 
        app.config.from_object(config_name_map[environment])
        blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
        api.init_app(blueprint)
        app.register_blueprint(blueprint)
        if environment == "development" or environment == "testing":  
            _create_local.seed()
    except Exception as err: 
        raise err 
