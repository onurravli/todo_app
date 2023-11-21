from django.urls import path, include
from .views import (
    handle_todo_by_id,
    handle_todos,
    index,
    delete_todos,
    delete_todo_by_id,
)

urlpatterns = [
    path("", index, name="index"),
    path("todos/", handle_todos, name="handle_todos"),
    path("todos/<int:id>", handle_todo_by_id, name="handle_todo_by_id"),
]
