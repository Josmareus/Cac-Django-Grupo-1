from django import forms
from .models import Escribano, ActoJuridico, Escritura
from django.core.exceptions import ValidationError
from django.forms import ModelForm  

class EscribanoForm(ModelForm):  
    class Meta:
        model = Escribano
        fields = ['escribano', 'caracter',]

    def __init__(self, *args, **kwargs):
        super(EscribanoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ActoJuridicoForm(ModelForm):  
    class Meta:
        model = ActoJuridico
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(ActoJuridicoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EscrituraForm(ModelForm):  
    class Meta:
        model = Escritura
        fields = ['fecha', 'escribano', 'folio', 'acto', 'otorgante', 'aceptante']

    def __init__(self, *args, **kwargs):
        super(EscrituraForm, self).__init__(*args, **kwargs)

        new_data1 = {
            "class": 'form-control'
        }
        new_data2 = {
            "class": 'form-select'
        }
        new_data3 = {
            "class": 'form-check-input'
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['escribano'].widget.attrs.update(new_data2)
        self.fields['acto'].widget.attrs.update(new_data2)