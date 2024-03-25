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
    busca = request.GET.get('alim')
    List = Produto.objects.filter(nome__contains=alim)
    if busca:
        List = Produto.objects.filter(nome__contains = busca)
    return render(request, 'exibir.html', {'List': List})

def nova(request, desc):
    busca = request.GET.get('desc')
    List = Produto.objects.filter(descricao__contains=desc)
    if busca:
        List = Produto.objects.filter(descricao__contains=busca)
    return render(request, 'exibir.html', {'List': List})
