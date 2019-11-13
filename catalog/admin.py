from django.contrib import admin
from .models import Category, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from administrator.admin import MenuItemsInline


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (MenuItemsInline,)


def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


activate.short_description = "Сделать активными"


def deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


deactivate.short_description = "Сделать неактивными"


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('title', 'category', 'price', 'is_active')
    list_filter = ('category', 'is_active')
    actions = [activate, deactivate, ]
