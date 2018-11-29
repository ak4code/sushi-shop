from django.contrib import admin
from .models import Shop, Link, Address, Phone, Page, Menu, MenuItem


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
    pass


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuItemInline,)
