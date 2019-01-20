from rest_framework import serializers
from .models import Cart, CartItem
from catalog.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    productInfo = ProductSerializer(source='product', many=False, read_only=True)
    amount = serializers.IntegerField(source='get_amount', read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.IntegerField(source='get_total', read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
