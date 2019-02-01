from django.contrib import admin
from .models import Order, Cart


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'phone', 'address', 'person', 'created')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
