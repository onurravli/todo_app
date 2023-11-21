from django.urls import path, include
from .views import get_todo_by_id, get_todos, index

urlpatterns = [
    path("", index, name="index"),
    path("todos/", get_todos, name="get_todos"),
    path("todos/<int:id>", get_todo_by_id, name="get_todo_by_id"),
]
