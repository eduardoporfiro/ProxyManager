from django.db import models
from core.models import AbstractDispositivo, AbstractDado, Task
from mqtt.models import Mqtt


class Dispositivo(AbstractDispositivo):
    mqtt = models.OneToOneField(Mqtt, on_delete=models.CASCADE, related_name='dispositivo')
    def __str__(self):
        return self.nome


class Dado(AbstractDado):
    sensor = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    def __str__(self):
        return "Dado: "+self.sensor.nome


class Job(models.Model):
    dispositivo = models.OneToOneField(Dispositivo, on_delete=models.CASCADE, related_name='job')
    workspace = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    firs_task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        self.firs_task.delete()
        super(Job, self).delete()

    def __str__(self):
        return 'Job: '+self.dispositivo.nome


class Atuador_troca_estado(Task):
    estado_anterior = models.NullBooleanField()
    estado_atual = models.NullBooleanField()
    atuador = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)


class Atuador_boolean(Task):
    estado = models.NullBooleanField()
    atuador = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)