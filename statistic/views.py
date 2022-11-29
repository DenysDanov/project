from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'statistic/index.html'

class SalesView(TemplateView):
    template_name = 'statistic/sales.html'

class MarginView(TemplateView):
    template_name = 'statistic/margin.html'