from django.urls import path
from .views import MenuView, CategoryView, ProductView

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    path('<slug>/', CategoryView.as_view(), name='category'),
    path('<slug>/<product_id>', ProductView.as_view(), name='product'),
]
