from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "garpix_page/index.html"
