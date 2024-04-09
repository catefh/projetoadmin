from django.shortcuts import render
from django.http import HttpResponse

from core.models import Produto, Categoria


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

    descricao = request.GET.get('descricao')
    if descricao:
        lista_de_produtos = lista_de_produtos.filter(descricao__contains=descricao)

    categoria = request.GET.get('categoria')
    if categoria:
        lista_de_produtos = lista_de_produtos.filter(categoria__nome__contains=categoria)
        
    return render(request, 'exibir.html', {'List': lista_de_produtos})


def listView (request, id):
    lista_de_produtos = Produto.objects.filter()

    produtos = request.GET.get('produtos')
    if produtos:
        lista_de_produtos = lista_de_produtos.filter(categoria_id__contains="")

    return render(request, 'idhtml.html', {'List': lista_de_produtos})