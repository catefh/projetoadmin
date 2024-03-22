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