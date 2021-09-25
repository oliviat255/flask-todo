import pytest 
from flask import url_for


def test_get_todos(flask_client, request_context): 
    with request_context: 
        response = flask_client.get(url_for("api.todo_todos"))
        assert response.status_code == 200 
        assert len(response.json) > 0

def test_new_todo_happy_path(flask_client, request_context): 
    with request_context: 
        data = {"title": "new test todo"}
        response = flask_client.post(url_for("api.todo_todos"), data=data)
        assert response.status_code == 201
        # retrieve new todo and assert response data 
        new_todo = flask_client.get(url_for("api.todo_todo_item", todo_id=response.json))
        assert new_todo.status_code == 200 
        assert new_todo.json["id"] == str(response.json)
        assert new_todo.json["title"] == data["title"]

def test_new_todo_sad_path(flask_client, request_context): 
    with request_context: 
        data = {"title": "todo 1"}
        response = flask_client.post(url_for("api.todo_todos"), data=data)
        assert response.status_code == 400

def test_get_todo_happy_path(flask_client, request_context): 
    with request_context: 
        response = flask_client.get(url_for("api.todo_todo_item", todo_id=1))
        assert response.status_code == 200

def test_get_nonexistent_todo(flask_client, request_context): 
    with request_context: 
        response = flask_client.get(url_for("api.todo_todo_item", todo_id=10))
        assert response.status_code == 404

def test_update_todo(flask_client, request_context): 
    with request_context: 
        response = flask_client.put(url_for("api.todo_todo_item", todo_id=1))
        assert response.status_code == 201
        assert response.json["id"] == "1"
        assert response.json["complete"] == True

def test_update_bad_todo(flask_client, request_context): 
    with request_context: 
        response = flask_client.put(url_for("api.todo_todo_item", todo_id=10))
        assert response.status_code == 404 

def test_delete_todo(flask_client, request_context): 
    with request_context: 
        todo_id = 1
        response = flask_client.delete(url_for("api.todo_todo_item", todo_id=todo_id))
        assert response.status_code == 204 
        
        todo = flask_client.get(url_for("api.todo_todo_item", todo_id=todo_id))
        assert todo.status_code == 404

def test_delete_nonexistent_todo(flask_client, request_context): 
    with request_context: 
        response = flask_client.delete(url_for("api.todo_todo_item", todo_id=10))
        assert response.status_code == 404