from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import LoginForm

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),
]
