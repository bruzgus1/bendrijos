from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bendrijos/', views.bendrijos_view, name='bendrijos'),
    path('add_bendrija/', views.add_bendrija_view, name='add_bendrija'),
    path('bendrijos_turinys/<bendrija_id>', views.bendrijos_turinys_view, name='bendrijos_turinys'),
    path('darbas_form/<bendrija_id>', views.add_darbas_view, name='darbas_form'),
    path('ataskaita_form/<bendrija_id>', views.add_ataskaita_view, name='ataskaita_form'),
    path('edit_bendrija/<bendrija_id>', views.edit_bendrija_view, name='edit_bendrija'),
]
