from django.views.generic import TemplateView
import pprint

class CartView(TemplateView):
    template_name = "shop/cart.html"

    def get(self, request, *args, **kwargs):
        request.session.create()
        pprint.pprint(request.session.session_key)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)