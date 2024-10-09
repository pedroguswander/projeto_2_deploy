from django.contrib import admin
from django.urls import path, include
from .views import login_view, cadastro_view, home_view, estoque_view

urlpatterns = [
    path('', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('home/', home_view, name='home'),
    path('estoque/', estoque_view, name='estoque'),
]