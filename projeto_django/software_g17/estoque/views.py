from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

def login_view(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
    return render(request, 'estoque/login.html')

def cadastro_view(request) :
    pass

def home_view(request) :
    qnt_materias = 0
    fantoches = 0
    context = {"qnt_materias" : qnt_materias, "fantoches" : fantoches}
    return render(request, 'estoque/home.html', context)
