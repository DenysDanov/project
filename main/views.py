from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name='index.html'

def handler500(request, template_name="500.html"):
    response = render(request, template_name)
    response.status_code = 500
    return response