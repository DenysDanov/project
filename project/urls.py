from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from main.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('main.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler500 = 'main.views.handler500'