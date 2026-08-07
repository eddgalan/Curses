from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from products.models import Product

from .models import Order, OrderItem


class OrderListViewTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            username="customer", password="A-secure-password-2026"
        )
        self.other_user = user_model.objects.create_user(
            username="another_customer", password="A-secure-password-2026"
        )
        self.user_order = Order.objects.create(
            user=self.user, status="Pending", total=Decimal("24.50")
        )
        self.other_order = Order.objects.create(
            user=self.other_user, status="Completed", total=Decimal("99.00")
        )

    def test_login_is_required(self):
        response = self.client.get(reverse("orders_list"))

        self.assertRedirects(
            response, f'{reverse("login")}?next={reverse("orders_list")}'
        )

    def test_only_logged_in_users_orders_are_listed(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("orders_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/orders_list.html")
        self.assertContains(response, f"Order #{self.user_order.pk}")
        self.assertNotContains(response, f"Order #{self.other_order.pk}")
        self.assertQuerySetEqual(response.context["orders"], [self.user_order])

    def test_empty_state_is_displayed_when_user_has_no_orders(self):
        user_without_orders = get_user_model().objects.create_user(
            username="new_customer", password="A-secure-password-2026"
        )
        self.client.force_login(user_without_orders)

        response = self.client.get(reverse("orders_list"))

        self.assertContains(response, "You don't have any orders yet")


class OrderDetailViewTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            username="customer", password="A-secure-password-2026"
        )
        self.other_user = user_model.objects.create_user(
            username="another_customer", password="A-secure-password-2026"
        )
        self.order = Order.objects.create(
            user=self.user, status="Pending", total=Decimal("25.00")
        )
        self.other_order = Order.objects.create(
            user=self.other_user, status="Completed", total=Decimal("10.00")
        )
        product = Product.objects.create(
            name="Cappuccino",
            description="Espresso with steamed milk",
            price=Decimal("12.50"),
        )
        OrderItem.objects.create(
            order=self.order,
            product=product,
            quantity=2,
            price=Decimal("12.50"),
            row_total=Decimal("25.00"),
        )

    def test_login_is_required(self):
        detail_url = reverse("order_details", args=[self.order.pk])

        response = self.client.get(detail_url)

        self.assertRedirects(response, f'{reverse("login")}?next={detail_url}')

    def test_detail_displays_items_and_totals(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("order_details", args=[self.order.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/order_detail.html")
        self.assertEqual(response.context["order"], self.order)
        self.assertContains(response, "Cappuccino")
        self.assertContains(response, "$12.50")
        self.assertContains(response, "$25.00")

    def test_user_cannot_view_another_users_order(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("order_details", args=[self.other_order.pk]))

        self.assertEqual(response.status_code, 404)
