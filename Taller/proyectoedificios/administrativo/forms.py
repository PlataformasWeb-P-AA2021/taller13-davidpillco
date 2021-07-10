from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo_edificio']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese la direccion por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
            'tipo_edificio': _('Seleccione el tipo de edificio por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese el nombre del edificio")
        return valor

    def clean_direccion(self):
        valor = self.cleaned_data['direccion']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese la direccion")
        return valor

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if len(valor) < 1:
            raise forms.ValidationError("Ingrese la ciudad")
        # Evaluacion del nombre de la ciudad
        if "L" in valor:
            raise forms.ValidationError("Ingrese ciudad valida")
        return valor

    def clean_tipo_edificio(self):
        valor = self.cleaned_data['tipo_edificio']
        if len(valor) < 1:
            raise forms.ValidationError("Seleccione un tipo de edificio")
        return valor

    

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nomPropietario', 'costo', 'num_cuartos', 'edificio']
    
    # Evaluacion de la cantidad de cuartos
    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        if (valor) == 0 or (valor) > 7:
            raise forms.ValidationError("Ingrese un numero de cuartos valido")
        return valor
    
    # Evaluacion del costo
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if (valor) > 100000:
            raise forms.ValidationError("Ingrese un costo valido")
        return valor

    def clean_nomPropietario(self):
        valor = self.cleaned_data['nomPropietario']
        num_palabras = len(valor.split())

        if num_palabras < 4:
            raise forms.ValidationError("Ingrese su nombre completo por favor")
        return valor

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nomPropietario', 'costo', 'num_cuartos', 'edificio']
    
    def clean_nomPropietario(self):
        valor = self.cleaned_data['nomPropietario']
        num_palabras = len(valor.split())

        if num_palabras < 4:
            raise forms.ValidationError("Ingrese su nombre completo por favor")
        return valor

    # Evaluacion de la cantidad de cuartos
    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        if (valor) == 0 or (valor) > 7:
            raise forms.ValidationError("Ingrese un numero de cuartos valido")
        return valor
        
    # Evaluacion del costo
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if (valor) > 100000:
            raise forms.ValidationError("Ingrese un costo valido")
        return valor