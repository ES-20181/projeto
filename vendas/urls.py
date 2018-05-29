from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('nova', views.nova_venda, name='nova'),
    path('buscar', views.buscar_vendas, name='buscar'),
    path('atualizar/<int:id>/', views.atualizar_venda, name='atualizar'),
    path('deletar/<int:id>/', views.deletar_venda, name='deletar'),
    path('historico', views.historico, name='historico'),
]
