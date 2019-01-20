from django.views.generic import TemplateView
import pprint

from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import ClientAppPermission
from rest_framework.response import Response

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartView(TemplateView):
    template_name = "shop/cart.html"

    def get(self, request, *args, **kwargs):
        pprint.pprint(request.session.session_key)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (ClientAppPermission,)

    @action(detail=False, methods=['post'])
    def init(self, request):
        session_key = request.session.session_key
        if session_key:
            cart = Cart.objects.get(session=session_key)
        else:
            request.session.create()
            cart = Cart.objects.create(session=request.session.session_key)
        serializer = self.get_serializer(cart, many=False)
        return Response(serializer.data)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (ClientAppPermission,)
