from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'fecha_incorporacion': 'Fecha de Incorporacion',
            'año_nacimiento': 'Año de Nacimiento',
            'telefono': 'Telefono',
            'email': 'Email',
            'sexo': 'Sexo',
            'estado': 'Estado',
            'observacion': 'Observacion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_incorporacion': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'año_nacimiento': forms.NumberInput(attrs={'class':'form-control'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-select'}),
            'estado': forms.Select(attrs={'class':'form-select'}),
            'observacion': forms.Textarea(attrs={'class':'form-control', 'rows':2}),
        }

    