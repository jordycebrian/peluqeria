from django.contrib import admin
from .models import Cita


#modificando el admin
class PostCita(admin.ModelAdmin):
    
    list_display = ['servicio','estilista','dia','hora','correo','nombre','telefono','cantidad','descripcion']
    readonly_fields = ['servicio','estilista','dia','hora','correo','nombre','telefono','cantidad','descripcion']


# Register your models here.

admin.site.register(Cita,PostCita)