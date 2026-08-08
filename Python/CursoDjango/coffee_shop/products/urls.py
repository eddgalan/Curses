from django.urls import path
from .views import ProductFormView, ProductListView, ProductListAPI

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("create/", ProductFormView.as_view(), name="create_product"),
    path("api/", ProductListAPI.as_view(), name="api_products_list"),
]
