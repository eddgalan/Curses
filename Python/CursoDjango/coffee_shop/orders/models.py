from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

from products.models import Product


class OrderStatus(models.TextChoices):
    QUOTE = "quote", "Quote"
    PENDING = "pending", "Pending"
    PROCESSING = "processing", "Processing"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"


class Order(models.Model):
    Status = OrderStatus

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user"],
                condition=Q(status=OrderStatus.QUOTE),
                name="unique_quote_per_user",
            ),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100,
        choices=OrderStatus.choices,
        default=OrderStatus.QUOTE,
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user} - {self.status}"

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["order", "product"],
                name="unique_product_per_order",
            ),
        ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    row_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (
            f"Order: {self.order} - Product: {self.product} - Quantity: {self.quantity}"
        )
