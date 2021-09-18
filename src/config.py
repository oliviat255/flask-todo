import os 

class DevConfig():
    """
    Configuration for local development
    """
    FLASK_APP = "wsgi.py"
    FLASK_ENV = "development"
    DEBUG = True