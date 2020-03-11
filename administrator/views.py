from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Page
from .serializers import PageSerializer


class HomeView(TemplateView):
    template_name = "administrator/home.html"


class PageView(TemplateView):
    template_name = "administrator/page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PageView, self).get_context_data(*args, **kwargs)
        page = get_object_or_404(Page, slug=context['url'])
        context['page'] = page
        return context


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
