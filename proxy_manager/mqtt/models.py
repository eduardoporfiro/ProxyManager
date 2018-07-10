from django.db import models
from django.utils import timezone

Qos = [
    (0, 'QoS - 0'),
    (1, 'QoS - 1'),
    (2, 'QoS - 2')
]
class Broker(models.Model):
    ESTADO_BROKER = (
        (0, 'Desligado'),
        (1, 'Iniciando'),
        (2, 'Rodando'),
        (3,'Com Problemas'),
        (4, 'Não Conectado'),
        (5, 'Parando')
    )
    endereco = models.CharField(max_length=200)
    porta = models.IntegerField(default=1883)
    user = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True)
    status = models.BooleanField(default=False)
    estado = models.IntegerField(choices=ESTADO_BROKER, default=0)

    def __str__(self):
        return self.endereco


class Mqtt(models.Model):
    broker = models.ForeignKey(Broker, on_delete=True)
    topico = models.CharField(max_length=250)
    QoS = models.IntegerField(choices=Qos, default=0)

    def __str__(self):
        return self.topico


class Dado(models.Model):
    mqtt = models.ForeignKey(Mqtt, on_delete=models.CASCADE)
    QoS = models.IntegerField(default=0, choices=Qos, editable=False)
    dado = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.mqtt.topico + " - " + self.dado
