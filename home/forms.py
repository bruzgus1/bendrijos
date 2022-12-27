from django import forms
from django.forms import ModelForm, TextInput
from .models import Bendrija


class BendrijaForm(forms.ModelForm):
    class Meta:
        model = Bendrija
        fields = ['name', 'address']
        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
            }),
            'address': TextInput(attrs={
                'type': 'text',
            }),
        }
