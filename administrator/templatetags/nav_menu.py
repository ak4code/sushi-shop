from django import template
from catalog.models import Category
from administrator.models import Menu

register = template.Library()


@register.inclusion_tag('administrator/primary_menu.html')
def primary_menu():
    menu = Menu.objects.get(location='primary')
    return {'menu': menu}


@register.inclusion_tag('administrator/catalog_menu.html')
def catalog_menu():
    categories = Category.objects.filter(is_home=True)
    return {'categories': categories}
