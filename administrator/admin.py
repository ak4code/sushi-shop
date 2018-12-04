from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from mptt.admin import DraggableMPTTAdmin

from .models import Shop, Link, Address, Phone, Page, Menu, MenuItem


class MenuItemsInline(GenericTabularInline):
    model = MenuItem
    extra = 1


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = (LinkInline, AddressInline, PhoneInline)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (MenuItemsInline,)


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(MenuItem)
class MenuItemAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuItemInline,)
