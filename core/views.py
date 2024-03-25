from django.shortcuts import render
from django.http import HttpResponse

from core.models import Produto


# Create your views here.
def index(request):
    lista = Produto.objects.all()
    context= {
        'lista': lista,
    }
    return render(request, 'index.html', context)

def pesquisa(request):
    lista_de_produtos = Produto.objects.filter()
    nome = request.GET.get('nome')
    if nome:
        lista_de_produtos = lista_de_produtos.filter(nome__contains=nome)
    return render(request, 'exibir.html', {'List': lista_de_produtos})

    
