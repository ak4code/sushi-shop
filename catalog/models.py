from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = HTMLField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/category', blank=True, null=True, verbose_name='Изображение')
    is_promo = models.BooleanField(default=False, verbose_name='Это акция?')
    is_home = models.BooleanField(default=False, verbose_name='Показывать на главной')
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name='Ссылка')

    def get_absolute_url(self):
        return reverse('catalog:category', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Раздел')
    short_desc = models.TextField(blank=True, null=True, verbose_name='Короткое описание')
    full_desc = models.TextField(blank=True, null=True, verbose_name='Полное описание')
    image = models.ImageField(upload_to='catalog/products', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'