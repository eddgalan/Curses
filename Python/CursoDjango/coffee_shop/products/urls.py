from django.urls import path
from .views import ProductListView, ProductListAPI

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("api/", ProductListAPI.as_view(), name="api_products_list"),
]
