from django.urls import path
from .views import home, venda

urlpatterns = [
    path('', home),
    path('venda/<int:codigo>/', venda),
]