from django.db import models
from django.contrib.sites.models import Site
from django.urls import reverse
from tinymce.models import HTMLField
from uuslug import uuslug


class Shop(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, verbose_name='Сайт')
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


class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    meta_description = models.TextField(verbose_name='Мета SEO описание')
    slug = models.SlugField(max_length=255, blank=True, null=True, verbose_name='Ссылка ЧПУ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.title, instance=self)
        super(Page, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
