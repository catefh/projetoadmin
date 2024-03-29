from django.conf import settings
from django.db import models




# Create your models here.
class Categoria(models.Model):
    nome= models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome