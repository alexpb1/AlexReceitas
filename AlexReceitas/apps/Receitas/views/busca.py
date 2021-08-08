from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import  User    
from Receitas.models import Receita

def buscar(request):
    lista_receitas=Receita.objects.order_by( '-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar=request.GET['buscar']
        if buscar:
            lista_receitas=lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    
    dados={
        'receitas':lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)

