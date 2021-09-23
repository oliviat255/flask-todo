import pytest 
from flask import Flask 
from src.app import create_app 

@pytest.fixture(scope="session")
def flask_app(): 
    """Fixture for a testing Flask app object""" 
    yield create_app("testing")

@pytest.fixture(scope="session")
def flask_client(flask_app: Flask):
    """Testing Flask client""" 
    return flask_app.test_client()

@pytest.fixture(scope="session")
def request_context(flask_app: Flask): 
    """Fixture for a flask app request context"""
    yield flask_app.test_request_context()