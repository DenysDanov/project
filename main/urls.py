from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPage.as_view()),
    path('scanner/', ScannerPage.as_view()),
    path('get_part_by_barcode/', PartByScanner.as_view()),
]