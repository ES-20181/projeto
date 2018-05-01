from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('listar_vendas', views.listar_vendas, name='listar_vendas'),
    path('nova', views.nova_venda, name='nova_venda'),
    path('atualizar/<int:id>/', views.atualizar_venda, name='atualizar_venda'),
    path('deletar/<int:id>/', views.deletar_venda, name='deletar_venda'),
]
