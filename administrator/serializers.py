from rest_framework import serializers
from .models import Page


class PageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Page
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()