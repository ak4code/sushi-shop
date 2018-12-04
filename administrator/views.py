from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from .models import Page
from django.views.defaults import page_not_found

class HomeView(TemplateView):
    template_name = "administrator/home.html"


class PageView(TemplateView):
    template_name = "administrator/page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PageView, self).get_context_data(*args, **kwargs)
        page = get_object_or_404(Page, slug=context['url'])
        context['page'] = page
        return context