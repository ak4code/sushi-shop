from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Category, Product

class MenuView(TemplateView):
    template_name = "catalog/menu.html"

class CategoryView(TemplateView):
    template_name = "catalog/category.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        category = get_object_or_404(Category, slug=context['slug'])
        context['category'] = category
        return context

class ProductView(TemplateView):
    template_name = "catalog/product.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        product = get_object_or_404(Product, id=context['product_id'])
        context['product'] = product
        return context