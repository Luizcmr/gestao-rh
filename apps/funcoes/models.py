from django.db import models
from django.urls import reverse

# Criando model funcao.
class Funcao(models.Model):
    nome = models.CharField(max_length=50, help_text="Nome da função")
    salario = models.CharField(max_length=50, help_text="Salário Base", null=True, blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('lista_funcoes')