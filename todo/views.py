from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Todo
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        JsonResponse(
            dict(message="ok"),
        ),
        status=200,
        content_type="application/json",
    )


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


@csrf_exempt
def add_todo(request: HttpRequest) -> HttpResponse:
    title = request.POST.get("title", "")
    desc = request.POST.get("desc", "")
    if not title or not desc:
        return HttpResponse(
            JsonResponse(
                dict(
                    error="Required fields missing.",
                ),
            ),
            status=400,
            content_type="application/json",
        )
    else:
        try:
            Todo.objects.create(
                title=title,
                desc=desc,
                done=False,
            )
            return HttpResponse(
                JsonResponse(
                    dict(
                        message="Todo added.",
                    ),
                ),
                status=201,
                content_type="application/json",
            )
        except Exception as ex:
            return HttpResponse(
                JsonResponse(
                    dict(
                        error="An error occurred.",
                        exception=ex.__str__(),
                    ),
                ),
                status=500,
                content_type="application/json",
            )


def delete_todos(request: HttpRequest) -> HttpResponse:
    try:
        Todo.objects.all().delete()
        return HttpResponse(
            JsonResponse(
                dict(message="All todos deleted."),
            ),
            status=200,
            content_type="application/json",
        )
    except Exception as ex:
        return HttpResponse(
            JsonResponse(
                dict(message="An error occurred."),
            ),
            status=500,
            content_type="application/json",
        )


@csrf_exempt
def handle_todos(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return get_todos(request=request)
    elif request.method == "POST":
        return add_todo(request=request)
    else:
        return HttpResponse(
            JsonResponse(
                dict(error="Method not allowed."),
            ),
            status=405,
            content_type="application/json",
        )
