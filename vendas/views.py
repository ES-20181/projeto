from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Venda
from .forms import VendaForm


def index(request):
    return render(request, 'vendas/index.html')


def historico(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/tables.html', {'vendas': vendas})


def register_teste(request):
    return render(request, 'vendas/register.html')


def forgot_password(request):
    return render(request, 'vendas/forgot-password.html')


def charts(request):
    return render(request, 'vendas/charts.html')


def blannk(request):
    return render(request, 'vendas/blank.html')


def login_teste(request):
    return render(request, 'vendas/login.html')
