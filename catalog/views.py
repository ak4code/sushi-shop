from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Category, Product
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer


class CategoryView(TemplateView):
    template_name = "catalog/category.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        category = get_object_or_404(Category, slug=context['slug'], is_active=True)
        context['category'] = category
        return context


class ProductView(TemplateView):
    template_name = "catalog/product.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        product = get_object_or_404(Product, id=context['product_id'], is_active=True)
        context['product'] = product
        return context


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    filter_fields = ('category',)
