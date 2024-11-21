from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('home/', home_view, name='home'),
    path('', brinquedos_view, name='brinquedos'),
    path('brinquedos_cadastro/', brinquedos_cadastro_view, name='brinquedos_cadastro'),
    path('brinquedo/<brinquedo_id>/', brinquedo_view, name='brinquedo'),
    path('estoque/', estoque_view, name='estoque'),
    path('estoque_pesquisa/<material_id>/', estoque_pesquisa_view, name='estoque_pesquisa'),
    path('estoque_adicionar/', estoque_adicionar_view, name='estoque_adicionar'),
]