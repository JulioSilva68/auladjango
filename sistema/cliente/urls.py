from django.urls import path

from . import views

app_name = "cliente" #dar um nome pra  url

urlpatterns = [
    path("", views.index, name="index"),
    path("hora/", views.hora, name="hora"),
    path("abacate/", views.abacate, name="Abacate"),
    

]