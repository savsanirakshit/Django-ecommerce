from django.contrib import admin
from .models import Item
from .models import Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'desc')


admin.site.register(Item, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)