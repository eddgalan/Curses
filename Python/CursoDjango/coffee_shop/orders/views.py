from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Sum
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import OrderItemForm
from .models import Order, OrderItem


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = "orders"
    template_name = "orders/orders_list.html"
    login_url = "login"

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .prefetch_related("items")
            .order_by("-created_at")
        )


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = "order"
    template_name = "orders/order_detail.html"
    login_url = "login"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related(
            "items__product"
        )


class AddProductToQuoteView(LoginRequiredMixin, View):
    login_url = "login"

    def post(self, request):
        form = OrderItemForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest("Invalid or unavailable product.")

        product = form.cleaned_data["product"]

        with transaction.atomic():
            order, _ = Order.objects.select_for_update().get_or_create(
                user=request.user,
                status=Order.Status.QUOTE,
                defaults={"total": Decimal("0.00")},
            )

            item, created = OrderItem.objects.select_for_update().get_or_create(
                order=order,
                product=product,
                defaults={
                    "quantity": 1,
                    "price": product.price,
                    "row_total": product.price,
                },
            )
            if not created:
                item.quantity += 1
                item.price = product.price
                item.row_total = product.price * item.quantity
                item.save(update_fields=("quantity", "price", "row_total"))

            order.total = order.items.aggregate(total=Sum("row_total"))[
                "total"
            ] or Decimal("0.00")
            order.updated_at = timezone.now()
            order.save(update_fields=("total", "updated_at"))

        return redirect("order_details", pk=order.pk)
