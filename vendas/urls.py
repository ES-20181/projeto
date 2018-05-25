from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tables', views.historico, name='historico'),
    path('login', views.login_teste, name='login'),
    path('charts', views.charts, name='charts'),
    # path('cards', name=''),
    # path('navbar', name=''),
    path('register', views.register_teste, name='register'),
    path('forget-password', views.forgot_password, name='forgot-password'),
    path('blank', views.blannk, name='blank'),
]
