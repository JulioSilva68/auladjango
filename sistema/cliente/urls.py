from django.urls import path

from . import views

app_name = "cliente" #dar um nome pra  url

urlpatterns = [
    path("", views.index, name="index"),
    path("hora/", views.hora, name="hora"),
    path("abacate/", views.abacate, name="Abacate"),
    path("cidade/", views.cidadeView, name="cidade"),
    path("cliente/", views.clienteView, name="cliente"),
    path("endereco/", views.enderecoView, name="endereco"),
    path("cadastro/", views.clienteView, name="cadastro"),
    path("busca/", views.clienteView, name="busca"),
]