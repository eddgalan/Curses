from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
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
            .exclude(status=Order.Status.QUOTE)
            .prefetch_related("items")
            .order_by("-created_at")
        )


class OrderCartView(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = "order"
    template_name = "orders/quote.html"
    login_url = "login"

    def get_object(self, queryset=None):
        order, created = Order.objects.get_or_create(
            user=self.request.user,
            status=Order.Status.QUOTE,
        )

        return (Order.objects
            .prefetch_related("items__product")
            .get(pk=order.pk)
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
                item.recalculate_row_total()

            order.recalculate_total()

        return redirect("cart")


class UpdateQuoteItemQuantityView(LoginRequiredMixin, View):
    login_url = "login"

    def post(self, request, pk):
        action = request.POST.get("action")
        if action not in {"increment", "decrement"}:
            return HttpResponseBadRequest("Invalid quantity action.")

        with transaction.atomic():
            item = get_object_or_404(
                OrderItem.objects.select_for_update().select_related("order"),
                pk=pk,
                order__user=request.user,
                order__status=Order.Status.QUOTE,
            )

            if action == "increment":
                item.quantity += 1
            elif item.quantity > 1:
                item.quantity -= 1

            item.recalculate_row_total()

            item.order.recalculate_total()

        return redirect("cart")


class DeleteQuoteItemView(LoginRequiredMixin, View):
    login_url = "login"

    def post(self, request, pk):
        with transaction.atomic():
            item = get_object_or_404(
                OrderItem.objects.select_for_update().select_related("order"),
                pk=pk,
                order__user=request.user,
                order__status=Order.Status.QUOTE,
            )
            order = item.order
            item.delete()
            order.recalculate_total()

        return redirect("cart")
