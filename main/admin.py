from django.contrib import admin

from .models import CarProducer, Auto, Part

class CustomAdminSite(admin.AdminSite):
    site_header = "Курсовий проект Дениса Курмана"
    site_title = 'FDA.if'
    index_title = 'FDA.if'

admin_site = CustomAdminSite(name='myadmin')

class PartPage(admin.ModelAdmin):
    search_fields = ['name', 'articul', 'belongs_to__model', 'belongs_to__producer__name']


admin_site.register(CarProducer)
admin_site.register(Part, PartPage)

class PartInline(admin.TabularInline):
    model = Part
    extra = 1

class AutoPage(admin.ModelAdmin):
    search_fields = ['vin', 'model']
    inlines = [
        PartInline,
    ]


admin_site.register(Auto, AutoPage)