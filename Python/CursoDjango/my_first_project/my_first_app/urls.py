from django.urls import path
from my_first_app.views import my_view, CarListView

urlpatterns = [
    path("list/", CarListView.as_view()),
    path("details/<int:id>", my_view),
]
