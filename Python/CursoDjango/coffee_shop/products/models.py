from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="name")
    description = models.TextField(verbose_name="description")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="price")
    available = models.BooleanField(default=True, verbose_name="available")
    photo = models.ImageField(upload_to="products", null=True, blank=True, verbose_name="photo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.name
