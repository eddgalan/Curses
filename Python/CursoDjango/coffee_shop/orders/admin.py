from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("id", "user", "status", "total", "created_at")
    search_fields = ('id', 'user__username', 'status')
    inlines = [OrderItemInLine]


admin.site.register(Order, OrderAdmin)
