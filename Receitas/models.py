from django.db import models
from datetime import datetime

from django.db.models.fields import DateTimeField

class Receita(models.Model):
    nome_receita=models.CharField(max_length=200)
    ingredientes=models.TextField(default='')
    modo_preparo= models.TextField(default='')
    tempo_preparo=models.IntegerField(default=0)
    rendimento=models.CharField(max_length=100)
    categoria=models.CharField(max_length=100)
    date_receita=models.DateTimeField(default=datetime.now, blank=True)

#def __str__(self): 
#    return self.nome_receita
