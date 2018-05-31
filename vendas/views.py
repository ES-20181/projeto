from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Venda
from .forms import VendaForm
from datetime import date


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            usuario = authenticate(nome=nome, senha=senha)
            login(request, usuario)
            redirect('dashboard')
        else:
            form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def dashboard(request):
    vendas = Venda.objects.filter(data=date.today()).order_by('-id')[:10]
    return render(request, 'vendas/dashboard.html', {'vendas': vendas})


def historico(request):
    vendas = Venda.objects.all().order_by('-id')
    return render(request, 'vendas/historico.html', {'vendas': vendas})


def nova_venda(request):
    form = VendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_vendas')

    return render(request, 'vendas/cad-venda.html', {'form': form})


def buscar_vendas(request):
    # vendas = Venda.objects.filter(id=id).order_by('-id')
    return render(request, 'vendas/busc-venda.html')


def buscar_id(request, id):
    codigo = int(request.GET.get("codigo"))
    vendas = Venda.objects.filter(id=codigo).order_by('-id')
    return render(request, 'vendas/busc-venda.html', {'vendas': vendas})


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
