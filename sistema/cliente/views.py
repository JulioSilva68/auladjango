from django.shortcuts import render

from django .http import HttpResponse 
from datetime import datetime

#Formulários
from .forms import CidadeForm
from .forms import ClienteForm
from .forms import EnderecoForm
from .forms import CadastraForm

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

def cidadeView(request):

    form = CidadeForm()

    context = {"form": form}


    return render(request, "cliente/cidade.html", context) 

def clienteView(request):

    form = ClienteForm()

    context = {"form": form}


    return render(request, "cliente/cliente.html", context)

def enderecoView(request):

    form = EnderecoForm()

    context = {"form": form}


    return render(request, "cliente/endereco.html", context)

def cadastraView(request):

    form = CadastraForm()

    context = {"form": form}
    
    return HttpResponse("Funciona")
