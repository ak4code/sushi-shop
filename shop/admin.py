from django.contrib import admin
from .models import Order, Cart


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)
