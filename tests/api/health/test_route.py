import pytest 
from flask import url_for

def test_healthcheck_get_status(flask_client, request_context): 
    """Test the healthcheck endpoint""" 
    with request_context: 
        response = flask_client.get(url_for("api.health_healthcheck"))
        assert response.status_code == 200 