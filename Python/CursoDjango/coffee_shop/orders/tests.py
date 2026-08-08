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


class AddProductToQuoteViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="customer", password="A-secure-password-2026"
        )
        self.product = Product.objects.create(
            name="Latte",
            description="Espresso with milk",
            price=Decimal("15.50"),
        )

    def test_login_is_required(self):
        response = self.client.post(
            reverse("add_product"), {"product": self.product.pk}
        )

        self.assertRedirects(
            response, f'{reverse("login")}?next={reverse("add_product")}'
        )

    def test_product_is_added_to_quote_and_redirects_to_detail(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("add_product"),
            {"product": self.product.pk, "price": "0.01", "quantity": "99"},
        )

        order = Order.objects.get(user=self.user, status=Order.Status.QUOTE)
        item = order.items.get(product=self.product)
        self.assertRedirects(response, reverse("order_details", args=[order.pk]))
        self.assertEqual(item.quantity, 1)
        self.assertEqual(item.price, self.product.price)
        self.assertEqual(item.row_total, self.product.price)
        self.assertEqual(order.total, self.product.price)

    def test_adding_same_product_increments_quantity_and_totals(self):
        self.client.force_login(self.user)
        add_product_url = reverse("add_product")

        self.client.post(add_product_url, {"product": self.product.pk})
        order = Order.objects.get(user=self.user, status=Order.Status.QUOTE)
        previous_updated_at = order.updated_at

        self.client.post(add_product_url, {"product": self.product.pk})

        order.refresh_from_db()
        item = order.items.get(product=self.product)
        self.assertEqual(order.items.count(), 1)
        self.assertEqual(item.quantity, 2)
        self.assertEqual(item.row_total, Decimal("31.00"))
        self.assertEqual(order.total, Decimal("31.00"))
        self.assertGreater(order.updated_at, previous_updated_at)

    def test_unavailable_product_is_rejected(self):
        self.client.force_login(self.user)
        self.product.available = False
        self.product.save(update_fields=("available",))

        response = self.client.post(
            reverse("add_product"), {"product": self.product.pk}
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(Order.objects.filter(user=self.user).exists())
