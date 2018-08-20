from django.db import models


class Tipo(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self): return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    quantidade_vidas = models.CharField(max_length=20, choices=(
        ('1', 'Uma'), ('2', 'Duas'), ('3',
                                      'Três'), ('4', 'Quatro'), ('5', 'Cinco ou mais')
    ))
    pessoa_tipo = models.ForeignKey(Tipo)

    def __str__(self): return self.nome

# CreatePersonMutation
