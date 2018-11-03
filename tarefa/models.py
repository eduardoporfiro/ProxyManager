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

class Task(models.Model):
    Tipos = [
        (0, 'save_database'),
        (1, 'dado_sensor_numero'),
        (2, 'dado_sensor_string'),
        (3, 'dados_sensor_media'),
        (4, 'dado_sensor_min'),
        (5, 'dado_sensor_max'),
        (6, 'if_sensor_string'),
        (7, 'if_sensor_numero'),
        (8, 'if_sensor_boolean'),
        (9, 'if_sensor_dadosensor'),
        (10, 'atuador_troca_estado'),
        (11, 'atuador_boolean')
    ]
    tipo = models.IntegerField(choices=Tipos, default=0)
    comando = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    task_anterior = models.ForeignKey('self', on_delete=models.CASCADE,
                                      related_name='anterior', null=True)
    task_sucessor = models.ForeignKey('self', on_delete=models.CASCADE,
                                      related_name='sucessor', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comando

    def start(self, payload, dipo_pk):
        if self.tipo == 0:
            dispo = Dispositivo.objects.get(pk=dipo_pk)
            if dispo.is_int:
                dado = Dado(sensor=dispo,
                            valor_int=int(payload))
                dado.save()
            else:
                dado = Dado(sensor=dispo,
                            valor_char=payload)
                dado.save()
        elif self.tipo == 1:
            try:
                return int(payload)
            except:
                return 0
        elif self.tipo == 2:
            return payload
        elif self.tipo == 3:
            return payload




class If_sensor_string(Task):
    Condicao = [
        (0,'='),
        (1,'!=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.CharField(max_length=200)


class If_sensor_numero(Task):
    Condicao = [
        (0, '='),
        (1, '!='),
        (2,'>'),
        (3,'>='),
        (4,'<'),
        (5,'<=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.IntegerField()

class If_sensor_dadosensor(Task):
    Condicao = [
        (0, '='),
        (1, '!='),
        (2, '>'),
        (3, '>='),
        (4, '<'),
        (5, '<=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='If_sensor_dadosensor')


class If_sensor_boolean(Task):
    Condicao = [
        (0, '='),
        (1, '!=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.NullBooleanField()


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