from django import forms
from django.forms import ModelForm, TextInput, DateInput
from .models import Bendrija, Atliktas_Darbas


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


class Atliktas_DarbasForm(forms.ModelForm):
    class Meta:
        model = Atliktas_Darbas
        fields = ['bendrija', 'pavadinimas', 'aprasymas', 'preliminari_kaina',
                  'galutine_kaina', 'atlikti_iki', 'darbas_atlikas',
                  'pastabos',]
        widgets = {
            'pavadinimas': TextInput(attrs={
                'type': 'text',
            }),
            'aprasymas': TextInput(attrs={
                'type': 'text',
            }),
            'preliminari_kaina': TextInput(attrs={
                'type': 'text',
            }),
            'galutine_kaina': TextInput(attrs={
                'type': 'text',
            }),
            'atlikti_iki': DateInput(attrs={
                'type': 'date',
            }),
            'darbas_atlikas': DateInput(attrs={
                'type': 'date',
            }),
            'pastabos': TextInput(attrs={
                'type': 'text',
            }),
        }
