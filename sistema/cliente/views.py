from django.shortcuts import render

from django .http import HttpResponse 
from datetime import datetime

# Create your views here.


def index(request):    
    return render(request, "cliente/index.html", {}) 

def hora(request):

    context = {"hora":datetime.now()}
     
    return render(request, "cliente/hora.html", context)

def abacate(request):
    nome = "Abacate"
    dtNascimento = "01/04/2020"
    cor = "verde"
    status = "verde"
    rg = "10"
    cpf = ""
    religiao = "budista"

    context ={
        "nome":nome,
        "dtNascimento":dtNascimento,
        "cor":cor,
        "status": status,
        "rg": rg,
        "cpf": cpf,
        "religiao": religiao
     
    }
    return render(request, "cliente/abacate.html", context) 