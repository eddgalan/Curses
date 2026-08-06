from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_editable = ('price', 'available')
    search_fields = ('name',)
    model = Product

admin.site.register(Product, ProductAdmin)
