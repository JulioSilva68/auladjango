from django.db import models

# Create your models here.
class Produto(models.Model):
    nm_produto = models.CharField(verbose_name="Nome do produto", max_length=25)
    emb_produto = models.CharField(verbose_name="Embalagem", max_length=5)
    id_produto = ???

class Estoque(models.Model):
    id_produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    tp_movimentacao = models.BooleanField(1/2)???
    dt_movimentacao = models.DateTimeField???