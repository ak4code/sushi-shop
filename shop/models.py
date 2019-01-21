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

    def __str__(self):
        return '{item.product.category}: {item.product.title} x {item.quantity} шт. = {amount} руб.'.format(item=self,
                                                                                                  amount=self.get_amount())


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя клиента')
    phone = models.CharField(max_length=255, verbose_name='Телефон клиента')
    address = models.CharField(max_length=255, verbose_name='Адрес клиента')
    person = models.PositiveIntegerField(verbose_name='Количество персон')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    send = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return 'Заказ {0}'.format(self.pk)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
