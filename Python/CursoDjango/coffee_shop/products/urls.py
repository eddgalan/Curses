from django.urls import path
from .views import ProductFormView

urlpatterns = [
    path("create/", ProductFormView.as_view(), name="create_product"),
]