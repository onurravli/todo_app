from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Todo
from django.core.exceptions import ObjectDoesNotExist


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        JsonResponse(
            dict(message="ok"),
        ),
        status=200,
        content_type="application/json",
    )


def add_todo(request: HttpRequest) -> HttpResponse:
    pass


def get_todos(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        JsonResponse(
            dict(
                todos=[
                    dict(
                        title=todo.title,
                        desc=todo.desc,
                        done=todo.done,
                        id=todo.pk,
                    )
                    for todo in Todo.objects.all()
                ]
            )
        ),
        status=200,
        content_type="application/json",
    )


def get_todo_by_id(request: HttpRequest, id: int) -> HttpResponse:
    try:
        _t = Todo.objects.get(pk=id)
        return HttpResponse(
            JsonResponse(
                dict(
                    title=_t.title,
                    desc=_t.desc,
                    done=_t.done,
                ),
            ),
            status=200,
            content_type="application/json",
        )
    except ObjectDoesNotExist as odne:
        return HttpResponse(
            JsonResponse(
                dict(
                    error="Todo not found",
                ),
            ),
            status=404,
            content_type="application/json",
        )
    except Exception as ex:
        return HttpResponse(
            JsonResponse(
                dict(
                    error="Unknown error occurred.",
                    ex=ex.__str__(),
                ),
            ),
            status=500,
            content_type="application/json",
        )
