import os

class DevConfig():
    """
    Configuration for local development
    """
    FLASK_APP = "app.py"
    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False