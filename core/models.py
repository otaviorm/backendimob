from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Anuncio(models.Model):
    titulo = models.CharField(max_length=100)
    qtd_quartos = models.IntegerField()
    qtd_banheiro = models.IntegerField()
    valor = models.FloatField()
    vagas = models.IntegerField(default=None, blank=True)
    descricao = models.CharField(max_length=100, default=None, blank=True)
    tamanho = models.IntegerField(default=None, blank=True)
    endereco = models.CharField(max_length=100, default=None, blank=True)

