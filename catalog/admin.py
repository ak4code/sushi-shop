from django.contrib import admin
from .models import Category, Product
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from administrator.admin import MenuItemsInline
from adminsortable2.admin import SortableAdminMixin


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
class ProductAdmin(SortableAdminMixin, ImportExportActionModelAdmin):
    resource_class = ProductResource
    list_display = ('position', 'title', 'category', 'price', 'is_active')
    list_display_links = ('title',)
    list_filter = ('category', 'is_active')
    search_fields = ('title',)
    actions = [activate, deactivate, ]
