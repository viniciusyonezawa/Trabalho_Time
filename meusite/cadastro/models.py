from django.db import models
from django.utils import timezone

class Time(models.Model) :
    nomeTime = models.CharField(max_length=50)
    estadio = models.CharField(max_length=50)
    patrocinio = models.CharField(max_length=50)
    nomeJogador = models.CharField(max_length=50)
    nomeTecnico = models.CharField(max_length=50)

    def __str__(self):
        return  self.nomeTime
