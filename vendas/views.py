from django.shortcuts import render
from .models import Venda

# Create your views here.


def home(request):
    nome = 'Testando'
    vendas = Venda.objects.all()
    return render(request, 'vendas.html', {'vendas': vendas})


def venda(request, codigo):
    venda = Venda.objects.get(id=codigo)
    return render(request, 'vendas.html', {'venda': venda})