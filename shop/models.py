from django.db import models


class Cart(models.Model):
    session = models.CharField(max_length=100, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def get_total(self):
        result = sum([item.get_amount() for item in self.items.all()])
        return result


class CartItem(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1, blank=True)

    def get_amount(self):
        result = self.product.price * self.quantity
        return result
