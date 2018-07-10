from django.db import models
from django.utils import timezone

class Broker(models.Model):
    ESTADO_BROKER = (
        (0, 'off'),
        (1, 'iniciating'),
        (2, 'running'),
        (3,'with problem'),
        (4, 'Not Conected')
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

    def __str__(self):
        return self.topico


class Dado(models.Model):
    Qos = [
        (0, 'QoS - 0'),
        (1, 'QoS - 1'),
        (2, 'QoS - 2')
    ]
    mqtt = models.ForeignKey(Mqtt, on_delete=models.CASCADE)
    QoS = models.IntegerField(default=0, choices=Qos, editable=False)
    dado = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.mqtt.topico + " - " + self.dado
