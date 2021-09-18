from flask import current_app
from flask_sqlalchemy import SQLAlchemy

class Client: 
    """
    Database client for SQLAlchemy 
    """
    def __init__(self): 
       self.client = SQLAlchemy(current_app)
       self.client.create_all()