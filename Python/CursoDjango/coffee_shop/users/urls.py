from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import LoginForm
from .views import register

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page="product_list"),
        name="logout",
    ),
    path("register/", register, name="register"),
]
