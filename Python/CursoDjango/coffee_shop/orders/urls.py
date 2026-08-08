from django.urls import path

from .views import AddProductToQuoteView, OrderDetailView, OrderListView

urlpatterns = [
    path("orders_list/", OrderListView.as_view(), name="orders_list"),
    path("order_details/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
    path("add_product/", AddProductToQuoteView.as_view(), name="add_product"),
]
