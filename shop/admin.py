from django.contrib import admin
from .models import Order, Cart


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'phone', 'address', 'person', 'created')


class CartCheckoutListFilter(admin.SimpleListFilter):
    title = 'Заказ'

    parameter_name = 'order'

    def lookups(self, request, model_admin):

        return (
            ('c', 'Оформленные'),
            ('n', 'Не оформленные'),
        )

    def queryset(self, request, queryset):

        if self.value() == 'c':
            return queryset.filter(order__isnull=False)
        if self.value() == 'n':
            return queryset.filter(order__isnull=True)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order', 'created')
    list_filter = (
        CartCheckoutListFilter,
    )
