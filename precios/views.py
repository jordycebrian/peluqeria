from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PreciosTabla, Ofertas


#visat a lista de precios
class PreciosListView(TemplateView):
    #asignando el template sino lo dara por defecto
    template_name = "preciostabla_list.html"

    #pasando la info de los modelos para mostrar las dos tablas
    def get_context_data(self, *args, **kwargs):
        cortes = PreciosTabla.objects.all()
        ofertas = Ofertas.objects.all()
        return {'cortes':cortes, 'ofertas':ofertas}





