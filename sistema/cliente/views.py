from django.shortcuts import render

from django .http import HttpResponse 
from datetime import datetime

#Formulários
from .forms import CidadeForm
from .forms import ClienteForm
from .forms import EnderecoForm

#Models
from .models import Cliente

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

    context = {}
    form = CidadeForm()
    context["form"] = form 

    if request.method == "POST":
        resultado = CidadeForm(request.POST)
        if resultado.is_valid():

            resultado.save()
            sucesso = "Registro salvo com sucesso"
            context["sucesso"] = sucesso
        else:
            
            erro = "Registro não foi salvo"
            context["erro"] = erro 

    return render(request, "cliente/cidade.html", context)                

    
def clienteView(request):

    context = {}
    form = ClienteForm()
    context["form"] = form

    if request.method== "POST":
        resultado = ClienteForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Cliente salvo com sucesso"
            context["sucesso"] = sucesso
        else:
            erro = "Cliente não foi salvo"
            context["erro"] = erro    
            
    
    return render(request, "cliente/cliente.html", context)

def enderecoView(request):

    form = EnderecoForm()

    context = {"form": form}


    return render(request, "cliente/endereco.html", context)

def clienteBusca(request):

    clientes = Cliente.objects.all()

    context = {"clientes": clientes}
    
    return render(request, "cliente/buscaCliente.html", context)
