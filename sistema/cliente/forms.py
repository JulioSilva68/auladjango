from django.forms import ModelForm

from .models import Cidade
from .models import Cliente
from .models import Endereco
from .models import Cadastra


class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = "__all__"

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"   

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__" 

class CadastraForm(ModelForm):
    class Meta:
        model = Cadastra
        fields = "__all__"       
