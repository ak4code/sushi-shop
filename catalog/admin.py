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


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('title', 'category', 'price')
    list_filter = ('category',)
