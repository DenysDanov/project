from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPage.as_view())
]