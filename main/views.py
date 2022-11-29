from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Part


class IndexPage(TemplateView):
    template_name='index.html'

class ScannerPage(TemplateView):
    template_name='scanner.html'

class PartByScanner(APIView):
    def post(self, request):
        barcode = request.data.get('barcode')
        if not barcode: 
            return Response({'error' : True, 'msg' : 'Missing barcode value'})
        try:
            part = Part.objects.get(barcode=barcode)
        except ObjectDoesNotExist:
            return Response({'error' : True, 'msg' : 'No parts with this barcode.\nTry again'})
        except Exception as e:
            return Response({'error' : True, 'msg' : f'{e}'})
        else:
            return Response({'error' : False, 'msg' : 'Success', 'data' : part.id })

def handler500(request, template_name="500.html"):
    response = render(request=request, template_name=template_name)
    response.status_code = 500
    return response