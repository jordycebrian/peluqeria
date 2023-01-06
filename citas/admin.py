from django.contrib import admin
from .models import Cita


#modificando el panel admin
class PostCita(admin.ModelAdmin):
    
    #campos visibles en el admin
    list_display = ['servicio','estilista','dia','hora','correo','nombre','telefono','cantidad','descripcion']
    #campos que solo se pueden ver, no editables
    readonly_fields = ['servicio','estilista','dia','hora','correo','nombre','telefono','cantidad','descripcion']


# Register your models here.

admin.site.register(Cita,PostCita)