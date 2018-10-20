from django.db import models
from core.models import AbstractDispositivo, AbstractDado
from mqtt.models import Mqtt

class Dispositivo(AbstractDispositivo):
    mqtt = models.OneToOneField(Mqtt, on_delete=models.CASCADE, related_name='dispositivo')
    def __str__(self):
        return self.nome

class Dado(AbstractDado):
    sensor = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    def __str__(self):
        return "Dado: "+self.sensor.nome
