from django.forms import ModelForm

from .models import Cidade
from .models import Cliente
from .models import Endereco



class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ["nm_cidade", "nm_estado", "nm_pais"]

        help_texts = {
            "nm_estado": ("*Preencher nome completo"),
            "nm_pais": ("*Preencher nome completo"),
        }

        labels = {
            "nm_cidade": "Nome da cidade",
            "nm_estado": "Nome do estado",
            "nm_pais": "Nome do pais",
        }

        error_messages = {
            "nm_cidade":{
                "max_length":"Nome da cidade muito longo",
                "required":"Campo obrigatório",
            }
        }

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nm_cliente", "nr_cpf", "dt_nascimento"]

        help_texts = {
            "nm_cliente": ("*Preencher nome completo"),
            "nr_cpf": ("*Preencher número completo"),
        }

        labels = {
            "nm_cliente": "Nome do cliente",
            "nr_cpf": "Número do cpf",
            "dt_nascimento": "Data de nascimento",
        }

        error_messages = {
            "nm_cliente":{
                "max_length":"Nome do cliente muito longo",
                "required":"Campo obrigatório",
            }
        }  

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ["tp_logradouro", "nm_logradouro", "nm_bairro"]
        
        help_texts = {
            "tp_logradouro": ("*Preencher nome completo"),
            "nm_logradouro": ("*Preencher nome completo"),
        }

        labels = {
            "tp_logradouro": "Tipo do logradouro",
            "nm_logradouro": "Nome do logradouro",
            "nm_bairro": "Nome do bairro",
        }

        error_messages = {
            "nm_logradouro":{
                "max_length":"Nome da cidade muito longo",
                "required":"Campo obrigatório",
            }
        } 
