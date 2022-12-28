from django.contrib import admin
from .models import Bendrija, Atliktas_Darbas

# Register your models here.


class BendrijaAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'name',
    )


class Atliktas_DarbasAdmin(admin.ModelAdmin):
    list_display = (
        'bendrija',
        'pavadinimas',
        'aprasymas',
        'preliminari_kaina',
        'galutine_kaina',
        'atlikti_iki',
        'darbas_atlikas',
        'pastabos',
    )


admin.site.register(Atliktas_Darbas, Atliktas_DarbasAdmin)
admin.site.register(Bendrija, BendrijaAdmin)
