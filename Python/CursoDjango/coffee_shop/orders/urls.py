from django.urls import path

from .views import (
    AddProductToQuoteView,
    DeleteQuoteItemView,
    OrderCartView,
    OrderDetailView,
    OrderListView,
    UpdateQuoteItemQuantityView,
)

urlpatterns = [
    path("orders_list/", OrderListView.as_view(), name="orders_list"),
    path("order_details/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
    path("cart/", OrderCartView.as_view(), name="cart"),
    path("add_product/", AddProductToQuoteView.as_view(), name="add_product"),
    path("cart/items/<int:pk>/quantity/", UpdateQuoteItemQuantityView.as_view(), name="update_quote_item_quantity"),
    path("cart/items/<int:pk>/delete/", DeleteQuoteItemView.as_view(), name="delete_quote_item"),
]
