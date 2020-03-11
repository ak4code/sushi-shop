from rest_framework import routers
from catalog.views import CategoryViewSet, ProductViewSet
from shop.views import CartViewSet, CartItemViewSet, OrderViewSet
from administrator.views import PageViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'pages', PageViewSet)
