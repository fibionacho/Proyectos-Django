from django.contrib import admin
from .models import Linea, Estaciones, Incidencia

# Register your models here.

class EstacionAdmin(admin.StackedInline):
    model = Estaciones

class LineaAdmin(admin.ModelAdmin):
    inlines =[EstacionAdmin]
    list_display =('nombre','color','distancia')

class IncidenteAdmin(admin.ModelAdmin):
    list_display = ('texto', 'fecha')
    list_filter = ['fecha']

admin.site.register(Linea, LineaAdmin)
admin.site.register(Estaciones)
admin.site.register(Incidencia, IncidenteAdmin)