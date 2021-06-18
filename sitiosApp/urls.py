from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',inicio, name='IND'),
    path('BASE', base, name='BASE'),
    path('SOLAYU', sol_ayu, name='SOLAYU'),
    path('MOTREC', mot_rec, name="MOTREC"),
    path('LOGIN', login, name='LOGIN'),
]
