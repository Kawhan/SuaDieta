from django import forms
from dietas.models import Dieta
from tempus_dominus.widgets import DatePicker
from datetime import datetime

class dietaform(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'
        widgets = {
            'data_final': DatePicker(),
            'data_inicio': DatePicker(),
            'pessoa': forms.HiddenInput,
        }


