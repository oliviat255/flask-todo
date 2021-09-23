"""Environment configuration"""

class DevConfig():
    """Configuration for local development"""
    FLASK_APP = "wsgi.py"
    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLACLHEMY_TRACK_MODIFICATIONS = False
