from django.urls import path, include
from .views import get_todo_by_id, handle_todos, index, delete_todos

urlpatterns = [
    path("", index, name="index"),
    path("todos/", handle_todos, name="handle_todos"),
    path("todos/<int:id>", get_todo_by_id, name="get_todo_by_id"),
    path("delete_todos/", delete_todos, name="delete_todos"),
]
