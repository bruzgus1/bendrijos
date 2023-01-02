from django import forms
from django.forms import ModelForm, TextInput, DateInput, NumberInput, Select
from .models import Bendrija, Atliktas_Darbas, Ataskaita


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


class AtaskaitaForm(forms.ModelForm):
    class Meta:
        model = Ataskaita
        fields = ['bendrija', 'year', 'mėnesis', 'atlyginimas', 'sodra', 'vmi', 'pvm_saskaitos_kvitas', 'bankines_operacijos']
        widgets = {
            'year': NumberInput(attrs={
                'type': 'number',
            }),
            'mėnesis': Select(attrs={'class': 'select'}),
            'atlyginimas': NumberInput(attrs={
                'type': 'number',
            }),
            'sodra': NumberInput(attrs={
                'type': 'number',
            }),
            'vmi': NumberInput(attrs={
                'type': 'number',
            }),
            'pvm_saskaitos_kvitas': NumberInput(attrs={
                'type': 'number',
            }),
            'bankines_operacijos': NumberInput(attrs={
                'type': 'number',
            }),
        }
