from django import forms
from .models import Escribano, ActoJuridico
from django.core.exceptions import ValidationError
from django.forms import ModelForm  

class EscribanoForm(ModelForm):  
    class Meta:
        model = Escribano
        fields = ['escribano', 'caracter',]

    def __init__(self, *args, **kwargs):
        super(EscribanoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'clase-css-aca'


class ActoJuridicoForm(ModelForm):  
    class Meta:
        model = ActoJuridico
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(ActoJuridicoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'clase-css-aca-2'