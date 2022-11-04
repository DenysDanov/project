from django.contrib import admin

from .models import CarProducer, Auto, Part

admin.site.register(CarProducer)
admin.site.register(Auto)
admin.site.register(Part)
