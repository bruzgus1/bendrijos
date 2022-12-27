from django.contrib import admin
from .models import Bendrija

# Register your models here.


class BendrijaAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'name',
    )


admin.site.register(Bendrija, BendrijaAdmin)