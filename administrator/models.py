from django.db import models
from django.contrib.sites.models import Site
from tinymce.models import HTMLField


class Shop(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logo', blank=True, null=True, verbose_name='Логотип')
    description = HTMLField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.site.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Link(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка')
    shop = models.ForeignKey('Shop', related_name='links', on_delete=models.CASCADE, verbose_name='Магазин')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'


class Address(models.Model):
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Номер дома')
    shop = models.ForeignKey('Shop', related_name='address', on_delete=models.CASCADE, verbose_name='Магазин')

    def get_full_address(self):
        return f'{self.city}, {self.street}, {self.house}'

    def __str__(self):
        return self.get_full_address()

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Phone(models.Model):
    number = models.CharField(max_length=255, verbose_name='Номер')
    is_primary = models.BooleanField(default=False, verbose_name='Главный')
    shop = models.ForeignKey('Shop', related_name='phones', on_delete=models.CASCADE, verbose_name='Магазин')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
