from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('home/', home_view, name='home'),
    path('brinquedos/', brinquedos_view, name='brinquedos'),
    path('brinquedos_cadastro/', brinquedos_cadastro_view, name='brinquedos_cadastro'),
    path('brinquedo/<brinquedo_id>/', brinquedo_view, name='brinquedo'),
    path('estoque/', estoque_view, name='estoque'),
]