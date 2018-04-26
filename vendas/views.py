from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm


def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas.html', {'vendas': vendas})


def nova_venda(request):
    form = VendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_vendas')

    return render(request, 'vendas-form.html', {'form': form})


def atualizar_venda(request, id):
    venda = Venda.objects.get(id=id)
    form = VendaForm(request.POST or None, instance=venda)

    if form.is_valid():
        form.save()
        return redirect('listar_vendas')

    return render(request, 'vendas-form.html', {'form': form, 'venda': venda})


def deletar_venda(request, id):
    venda = Venda.objects.get(id=id)

    if request.method == 'POST':
        venda.delete()
        return redirect('listar_vendas')

    return render(request, 'venda-deletar-confirm.html', {'venda': venda})
