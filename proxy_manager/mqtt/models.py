from django.db import models


class Broker(models.Model):
    ESTADO_BROKER = (
        (0, 'off'),
        (1, 'on'),
        (2, 'running')
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


class Dado(models.Model):
    mqtt = models.ForeignKey(Mqtt, on_delete=models.CASCADE)
    dado = models.CharField(max_length=200)
