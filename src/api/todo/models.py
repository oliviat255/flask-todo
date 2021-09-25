from flask_restx import fields, Model # type: ignore

# todo model 
todo_model_def = Model('Todo', {
    "id": fields.String, 
    "title": fields.String,
    "complete": fields.Boolean
})

# todo list model 
todo_list_model_def = Model("TodoList", {
    "todos": fields.List(fields.Nested(todo_model_def))
})

