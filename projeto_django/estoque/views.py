from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .models import Material, Brinquedo, material_de_um_brinquedo

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

def brinquedos_view(request) :
    brinquedos = Brinquedo.objects.all()
    context = {'brinquedos' : brinquedos}
    return render(request, 'estoque/brinquedos.html', context)


def brinquedos_cadastro_view(request) :
    materiais = Material.objects.all()

    if request.method == 'POST':
        brinquedo = request.POST.get('brinquedo')
        descricao = request.POST.get('descricao')
        passo_a_passo = request.POST.get('passo a passo')

        b = Brinquedo(
            brinquedo = brinquedo,
            descricao = descricao,
            passo_a_passo = passo_a_passo,
        )
        b.save()

        for material in materiais:
            if request.POST.get(f'material_{material.id}') == 'on':
                quantidade = request.POST.get(f'quantidade_{material.id}')
                if quantidade:
                    m = material_de_um_brinquedo(
                        brinquedo=b,
                        material=material.material,
                        quantidade=int(quantidade),
                    )
                    m.save()

        return redirect('brinquedos')
    
    context = {'materiais': materiais}
    return render(request, 'estoque/brinquedos_cadastro.html', context)

def brinquedo_view(request, brinquedo_id) :
    preco_total = 0
    pode_produzir = True
    faltando = []

    brinquedo = Brinquedo.objects.get(id = brinquedo_id)
    materiais = material_de_um_brinquedo.objects.filter(brinquedo = brinquedo)
    for material in materiais :
        material_do_estoque = Material.objects.get(material = material)
        preco_total += material.quantidade * material_do_estoque.preco

        if material.quantidade > material_do_estoque.quantidade:
            pode_produzir = False
            faltando.append(f'{material}: faltam {material.quantidade - material_do_estoque.quantidade} itens, você possui {material_do_estoque.quantidade} item no estoque')

    
    context = {'brinquedo' : brinquedo, 'materiais' : materiais, 'preco_total' : preco_total,
            'pode_produzir' : pode_produzir, 'faltando' : faltando,}
    
    return render(request, 'estoque/brinquedo.html', context)

def estoque_view(request) :
    error_message = ''

    if request.method == 'POST' :
        if request.POST.get('pesquisa_material') == 'pesquisa_material':
            material = request.POST.get("pesquise por materiais")
            try:
                material_filtrado = Material.objects.get(material__iexact = material)
                return redirect('estoque_pesquisa', material_filtrado)
            
            except Material.DoesNotExist:
                error_message = 'Material não encontrado!'
            
        if request.POST.get("registrar_material") == "registrar_material":
            material = request.POST.get('material')
            quantidade = request.POST.get('quantidade')
            preco = request.POST.get('preco')
            date_added = request.POST.get('date_added')

            m = Material(
                material = material,
                quantidade = quantidade,
                preco = preco,
                date_added = date_added,
            )

            m.save()

    materiais = Material.objects.all()

    for material in materiais :
        material.valor = material.quantidade * material.preco

    context = {'materiais' : materiais, 'error_message': error_message}

    return render(request, 'estoque/estoque.html', context)

def estoque_pesquisa_view(request, material_id) :
    context = {'material_filtrado': material_id,}
    return render(request, 'estoque/estoque_pesquisa.html', context)