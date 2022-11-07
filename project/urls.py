from django.urls import include, path

from main.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('main.urls'))
]
handler500 = 'main.views.handler500'