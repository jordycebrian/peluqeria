
from django.views.generic import CreateView
from django import forms
from .form import CitaForm
from django.urls import reverse_lazy

# Create your views here.


##Vista para citas###
class Citas(CreateView):
    # llamando form y asignando plantilla
    form_class = CitaForm
    template_name = 'citas.html'


    #redireccion a enlace una vez completado formlario
    def get_success_url(self) -> str:
        return reverse_lazy('citas')



    #editando el formulario en tiempo real
    def get_form(self, form_class=None):
        form = super(Citas, self).get_form()


        #modificacion timpo real
        form.fields['servicio'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre del Servicio ejemplo: Corte, Barba'})
        form.fields['estilista'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre del Estilista(opcional)'})
        form.fields['dia'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Dia'})
        form.fields['hora'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Hora'})
        form.fields['correo'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Correo'})
        form.fields['nombre'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre'})
        form.fields['telefono'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Telefono'})
        form.fields['cantidad'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Cantidad de personas'})
        form.fields['descripcion'].widget = forms.Textarea(attrs={'class':'form-control mb-2','placeholder':'Descripción(Opcional)'})
        
        return form
        