from django.urls import path
from .views import listar_vendas, nova_venda, atualizar_venda, deletar_venda

urlpatterns = [
    path('', listar_vendas, name='listar_vendas'),
    path('nova', nova_venda, name='nova_venda'),
    path('atualizar/<int:id>/', atualizar_venda, name='atualizar_venda'),
    path('deletar/<int:id>/', deletar_venda, name='deletar_venda'),
]
