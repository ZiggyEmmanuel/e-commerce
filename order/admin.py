#order/admin

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'is_paid', 'status')
    list_filter = ('is_paid', 'status', 'created_at')
    search_fields = ('user__email',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('order', 'product')
    search_fields = ('product__name', 'order__id')
    readonly_fields = ('price',)
