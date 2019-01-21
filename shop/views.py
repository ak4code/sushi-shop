from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import ClientAppPermission
from rest_framework.response import Response
from administrator.vkbot import send_order
from .models import Cart, CartItem, Order
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer


class CartView(TemplateView):
    template_name = "shop/cart.html"

    def get(self, request, *args, **kwargs):
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
            cart, created = Cart.objects.get_or_create(session=session_key)
        else:
            request.session.create()
            cart = Cart.objects.create(session=request.session.session_key)
        serializer = self.get_serializer(cart, many=False)
        return Response(serializer.data)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (ClientAppPermission,)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (ClientAppPermission,)

    def perform_create(self, serializer):
        instance = serializer.save(send=True)
        inputs = ['%s' % (item) for item in instance.cart.items.all()]
        items = '\n'.join(inputs)
        message = '''Новый заказ
        Имя: {order.name}
        Телефон: {order.phone}
        Адрес: {order.address}
        Количество персон: {order.person}
        Сумма: {total} руб.
        ЗАКАЗ: \n {items!s} 
        '''.format(order=instance, total=instance.cart.get_total(), items=items)
        send_order(message)
        self.request.session.create()