from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('nova', views.nova_venda, name='nova_venda'),
    path('buscar_vendas', views.buscar_vendas, name='buscar_vendas'),
    path('atualizar/<int:id>/', views.atualizar_venda, name='atualizar_venda'),
    path('deletar/<int:id>/', views.deletar_venda, name='deletar_venda'),
    path('login', views.login, name='login'),
]
