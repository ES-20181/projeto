from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm
# import time


def dashboard(request):
    vendas = Venda.objects.all()
    # ultimas_vendas = []
    # for venda in vendas:
    #     for i in range(5):
    #         ultimas_vendas.append(venda)
    return render(request, 'vendas/dashboard.html',
                  {'vendas': vendas})


def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/vendas.html', {'vendas': vendas})


def nova_venda(request):
    form = VendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_vendas')

    return render(request, 'vendas/vendas-form.html', {'form': form})


def atualizar_venda(request, id):
    venda = Venda.objects.get(id=id)
    form = VendaForm(request.POST or None, instance=venda)

    if form.is_valid():
        form.save()
        return redirect('listar_vendas')

    return render(request, 'vendas/vendas-form.html',
                  {'form': form, 'venda': venda})


def deletar_venda(request, id):
    venda = Venda.objects.get(id=id)

    if request.method == 'POST':
        venda.delete()
        return redirect('listar_vendas')

    return render(request,
                  'vendas/venda-deletar-confirm.html',
                  {'venda': venda})


def login(request):
    # time.sleep(5)
    # if True:
    #     return redirect('dashboard')
    return render(request, 'vendas/login.html')
