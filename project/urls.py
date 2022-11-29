from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from main.admin import admin_site
from main.views import handler500 as h500
import re
from django.views.static import serve
urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('main.urls')),
    path('stats/', include('statistic.urls')),
    re_path( r"^%s(?P<path>.*)$" % re.escape(settings.STATIC_URL.lstrip("/")), view=serve, kwargs = {'document_root':settings.STATIC_ROOT})
]
if settings.DEBUG:
    urlpatterns.append(path('500/', h500))

handler500 = 'main.views.handler500'