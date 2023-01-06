from django import forms
from .models import Cita
from django.forms import ValidationError


#form para cita
class CitaForm(forms.ModelForm):

    #formato de campoas para cita
    class Meta:
        model = Cita

        fields = ['servicio','estilista','dia','hora','correo','nombre','telefono','cantidad','descripcion']

        widgets = {
            'servivcio':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Servicios'}),
            'estilista':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estilista'}),
            'dia':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dia'}),
            'hora':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hora'}),
            'correo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo'}),
            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'nombre'}),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cantidad'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripción'}),
        }



    #avisar de que la hora ya esta reservada  
    def clean_hora(self):
        hora = self.cleaned_data['hora']
        exists = Cita.objects.filter(hora=hora).exists()

        if exists:
            raise ValidationError("Esta hora ya esta ocupada, intenta otro horario")
        return hora