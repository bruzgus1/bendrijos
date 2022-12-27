from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bendrijos/', views.bendrijos_view, name='bendrijos'),
    path('add_bendrija/', views.add_bendrija_view, name='add_bendrija'),
]
