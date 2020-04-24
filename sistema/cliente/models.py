from django.db import models

# Create your models here.

class Cidade(models.Model):
    nm_cidade = models.CharField(max_length=20)
    nm_estado = models.CharField(max_length=15)    
    sg_estado = models.CharField(max_length=2)
    nm_pais = models.CharField(max_length=10)
    sg_pais = models.CharField(max_length=3)
    
    def _str_(self):
        return self.nm_cidade + " - " + self.sg_estado
    

class Endereco(models.Model):
    tp_logradouro = models.CharField(max_length=15)
    nm_logradouro = models.CharField(max_length=40)
    nm_bairro = models.CharField(max_length=20)
    cd_cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nm_logradouro
    

class Cliente(models.Model):
    nm_cliente = models.CharField(verbose_name="Nome do Cliente", max_length=45)
    nr_cpf = models.CharField(verbose_name="Número do CPF",max_length=14)
    dt_nascimento = models.DateField(verbose_name="Data de nascimento")
    idade = models.IntegerField(verbose_name="Idade")
    nr_endereco = models.IntegerField()
    dsc_complemento = models.TextField()
    cd_endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)

    def __str__(self):
        return self.nm_cliente 


