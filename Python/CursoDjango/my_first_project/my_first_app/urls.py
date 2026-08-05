from django.http import HttpResponse

from django.urls import path

def my_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

urlpatterns = [
    path("list/", my_view),
    path("details/<int:id>", my_view),
]
