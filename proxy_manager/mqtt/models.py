from django.db import models
from django.utils import timezone
from django.contrib import messages
from solo.models import SingletonModel

Qos = [
    (0, 'QoS - 0'),
    (1, 'QoS - 1'),
    (2, 'QoS - 2')
]
class Broker(SingletonModel):
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
    RC = [
        (0,'Conexão Aceita'),
        (1,'Conexão Recusada, Versão de Protocolo não aceita'),
        (2,'Conexão Recusada, identificador recusado'),
        (3, 'Conexão Recusada, servidor indisponível'),
        (4, 'Conexão Recusada, Usuário ou Senha inválido'),
        (5, 'Conexão Recusada, conexão não autorizada'),
    ]
    broker = models.ForeignKey(Broker, on_delete=True)
    topico = models.CharField(max_length=250)
    QoS = models.IntegerField(choices=Qos, default=0)
    RC = models.IntegerField(choices=RC, default=0)
    def __str__(self):
        return self.topico

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Mqtt, self).save()
        self.reinicia_broker()

    def delete(self, using=None, keep_parents=False):
        super(Mqtt, self).delete()
        self.reinicia_broker()

    def reinicia_broker(self):
        self.broker.estado = 4
        self.broker.save()
        import mqtt.tasks as task
        task.restart.delay()


class Dado(models.Model):
    mqtt = models.ForeignKey(Mqtt, on_delete=models.CASCADE)
    QoS = models.IntegerField(default=0, choices=Qos, editable=False)
    dado = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.mqtt.topico + " - " + self.dado
