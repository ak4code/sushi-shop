from django.urls import path
from .views import CategoryView, ProductView

urlpatterns = [
    path('<slug>/', CategoryView.as_view(), name='category'),
    path('<slug>/<product_id>', ProductView.as_view(), name='product'),
]
