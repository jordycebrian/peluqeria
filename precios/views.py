from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PreciosTabla, Ofertas



class PreciosListView(TemplateView):
    template_name = "preciostabla_list.html"

    #pasando la info de los modelos
    def get_context_data(self, *args, **kwargs):
        cortes = PreciosTabla.objects.all()
        ofertas = Ofertas.objects.all()
        return {'cortes':cortes, 'ofertas':ofertas}





