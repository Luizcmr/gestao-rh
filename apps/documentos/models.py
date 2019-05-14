from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario

# Criando model documentos.
class Documento(models.Model):
    descricao = models.CharField(max_length=50, help_text="Descrição do documento")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to="documentos")

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('edit_funcionario', args=[self.funcionario.id])