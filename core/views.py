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

def pesquisa(request, alim):
    lista_de_produtos = Produto.objects.filter(nome__contains=)
    return render(request, 'exibir.html', {'List': lista_de_produtos})

def nova(request, desc):
    lista_de_produtos = Produto.objects.filter(descricao__contains=)
    return render(request, 'exibir.html', {'List': lista_de_produtos})
