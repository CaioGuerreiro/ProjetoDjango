from django.db import models
from datetime import datetime

# Create your models here.

class fotografia(models.Model):

    opcoes_categoria = [("NEBULOSA", "nebulosa"), ("ESTRELA", "estrela"), ("GALAXIA", "galaxia"), ("PLANETA", "planeta"),]

    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda = models.CharField(max_length = 150, null = False, blank = False)
    categoria = models.CharField(max_length = 100, choices = opcoes_categoria, default = '')
    descricao = models.TextField(null = False, blank = False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    publicada = models.BooleanField(default = False)
    data_publicada = models.DateTimeField(default = datetime.now, blank = False)

    def __str__(self):
        return self.nome
