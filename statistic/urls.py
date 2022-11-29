from django.urls import path

from .views import IndexPage,SalesView,MarginView

urlpatterns = [
    path('sales/', SalesView.as_view()),
    path('', IndexPage.as_view()),
    path('margin/', MarginView.as_view()),
]