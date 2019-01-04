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
        (11, 'atuador_boolean'),
        (12, 'if_else_sensor_string'),
        (13, 'if_else_sensor_boolena'),
        (14, 'if_else_sensor_dadosensor'),
        (15, 'if_else_sensor_number')
    ]
    tipo = models.IntegerField(choices=Tipos, default=0)
    comando = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    task_anterior = models.ForeignKey('self', on_delete=models.CASCADE,
                                      related_name='anterior', null=True, blank=True)
    task_sucessor = models.ForeignKey('self', on_delete=models.CASCADE,
                                      related_name='sucessor', null=True, blank=True)
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
            print('Dado Salvo')
            if self.task_sucessor:
                self.task_sucessor.start(payload, dipo_pk)
        elif self.tipo == 1:
            try:
                return int(payload)
            except:
                return 0
        elif self.tipo == 2:
            return payload
        elif self.tipo == 3:
            dispo = Dispositivo.objects.get(pk=dipo_pk)
            if dispo.is_int:
                avg = Dado.objects.filter(sensor=dispo).aggregate(models.Avg('valor_int'))
                return avg['valor_int__avg']
            else:
                avg = Dado.objects.filter(sensor=dispo).aggregate(models.Avg('valor_char'))
                return avg['valor_char__avg']
        elif self.tipo == 4:
            dispo = Dispositivo.objects.get(pk=dipo_pk)
            if dispo.is_int:
                min = Dado.objects.filter(sensor=dispo).aggregate(models.Min('valor_int'))
                return min['valor_int__min']
            else:
                min = Dado.objects.filter(sensor=dispo).aggregate(models.Min('valor_char'))
                return min['valor_char__min']
        elif self.tipo == 5:
            dispo = Dispositivo.objects.get(pk=dipo_pk)
            if dispo.is_int:
                max = Dado.objects.filter(sensor=dispo).aggregate(models.Max('valor_int'))
                return max['valor_int__max']
            else:
                max = Dado.objects.filter(sensor=dispo).aggregate(models.Max('valor_char'))
                return max['valor_char__max']
        elif self.tipo == 6:
            If_sensor_string.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 7:
            If_sensor_numero.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 8:
            If_sensor_boolean.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 9:
            If_sensor_dadosensor.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 10:
            Atuador_troca_estado.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 11:
            Atuador_boolean.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 12:
            If_else_sensor_string.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 13:
            If_else_sensor_boolean.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 14:
            If_else_sensor_dadosensor.objects.filter(pk=self.pk).get().start(payload, dipo_pk)
        elif self.tipo == 15:
            If_else_sensor_numero.objects.filter(pk=self.pk).get().start(payload, dipo_pk)


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


class If_sensor_string(Task):
    Condicao = [
        (0, '='),
        (1, '!=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.CharField(max_length=200)

    def start(self, payload, dipo_pk):
        if self.task_sucessor is not None:
            if self.condicao == 0:
                if payload == self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
            else:
                if payload != self.valor:
                    self.task_sucessor.start(payload, dipo_pk)


class If_else_sensor_string(Task):
    Condicao = [
        (0, '='),
        (1, '!=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.CharField(max_length=200)
    elsetask = models.ForeignKey(Task, on_delete=models.CASCADE,
                                      related_name='elsetasksensor_string', null=True)

    def start(self, payload, dipo_pk):
        if self.task_sucessor is not None:
            if self.condicao == 0:
                if payload == self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)
            else:
                if payload != self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)


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

    def start(self, payload, dipo_pk):
        print('NUMERO:TRUE')
        if self.task_sucessor is not None:
            print('NUMERO:TRUE')
            if self.condicao == 0:
                if self.valor == int(payload):
                    print('NUMERO:TRUE')
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 1:
                if self.valor != int(payload):
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 2:
                if int(payload) > self.valor:
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 3:
                if int(payload) >= self.valor:
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 4:
                if int(payload) < self.valor:
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 5:
                if int(payload) <= self.valor:
                    self.task_sucessor.start(payload, dipo_pk)


class If_else_sensor_numero(Task):
    Condicao = [
        (0, '='),
        (1, '!='),
        (2, '>'),
        (3, '>='),
        (4, '<'),
        (5, '<=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.IntegerField()
    elsetask = models.ForeignKey(Task, on_delete=models.CASCADE,
                                 related_name='elsetasksensor_numero', null=True)

    def start(self, payload, dipo_pk):
        if self.task_sucessor is not None:
            if self.condicao == 0:
                if self.valor == int(payload):
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 1:
                if self.valor != int(payload):
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 2:
                if int(payload) > self.valor:
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 3:
                if int(payload) >= self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 4:
                if int(payload) < self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 5:
                if int(payload) <= self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)


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

    def start(self, payload, dipo_pk):
        if self.valor is not None and self.task_sucessor is not None:
            if self.condicao == 0:
                if payload == self.valor.start(payload, dipo_pk):
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 1:
                if payload != self.valor.start(payload, dipo_pk):
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 2:
                if self.valor.start(payload, dipo_pk) > payload:
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 3:
                if self.valor.start(payload, dipo_pk) >= payload:
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 4:
                if self.valor.start(payload, dipo_pk) < payload:
                    self.task_sucessor.start(payload, dipo_pk)

            elif self.condicao == 5:
                if self.valor.start(payload, dipo_pk) <= payload:
                    self.task_sucessor.start(payload, dipo_pk)


class If_else_sensor_dadosensor(Task):
    Condicao = [
        (0, '='),
        (1, '!='),
        (2, '>'),
        (3, '>='),
        (4, '<'),
        (5, '<=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='If_else_sensor_dadosensor')
    elsetask = models.ForeignKey(Task, on_delete=models.CASCADE,
                                 related_name='elsetasksensor_dadosensor', null=True)

    def start(self, payload, dipo_pk):
        if self.valor  is not None and self.task_sucessor is not None:
            if self.condicao == 0:
                if payload == self.valor.start(payload, dipo_pk):
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 1:
                if payload != self.valor.start(payload, dipo_pk):
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 2:
                if self.valor.start(payload, dipo_pk) > payload:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 3:
                if self.valor.start(payload, dipo_pk) >= payload:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 4:
                if self.valor.start(payload, dipo_pk) < payload:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)

            elif self.condicao == 5:
                if self.valor.start(payload, dipo_pk) <= payload:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)


class If_sensor_boolean(Task):
    Condicao = [
        (0, '='),
        (1, '!=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.NullBooleanField()

    def start(self, payload, dipo_pk):
        if self.task_sucessor is not None:
            if self.condicao == 0:
                if bool(payload) == self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
            else:
                if bool(payload) != self.valor:
                    self.task_sucessor.start(payload, dipo_pk)


class If_else_sensor_boolean(Task):
    Condicao = [
        (0, '='),
        (1, '!=')
    ]
    condicao = models.IntegerField(choices=Condicao)
    valor = models.NullBooleanField()
    elsetask = models.ForeignKey(Task, on_delete=models.CASCADE,
                                 related_name='elsetasksensor_boolean', null=True)

    def start(self, payload, dipo_pk):
        if self.task_sucessor is not None:
            if self.condicao == 0:
                if bool(payload) == self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)
            else:
                if bool(payload) != self.valor:
                    self.task_sucessor.start(payload, dipo_pk)
                else:
                    if self.elsetask is not None:
                        self.elsetask.start(payload, dipo_pk)


class Atuador_troca_estado(Task):
    estado_anterior = models.BooleanField(default=True, null=True)
    estado_atual = models.BooleanField(default=False, null=True)
    atuador = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.estado_anterior is None:
            self.estado_anterior = True
        if self.estado_atual is None:
            self.estado_atual = False
        super(Atuador_troca_estado, self).save()

    def start(self, payload, dipo_pk):
        print("Atuador Troca Estado")
        if self.atuador is not None:
            try:
                self.envia_mqtt(self.atuador.mqtt.topico, self.estado_anterior)
                atual = self.estado_atual
                self.estado_atual = self.estado_anterior
                self.estado_anterior = atual
                self.save()
            except Exception as e:
                print(e)

        if self.task_sucessor is not None:
            self.task_sucessor.start(payload, dipo_pk)

    def envia_mqtt(self, topico, valor):
        import paho.mqtt.publish as publish
        if self.atuador.mqtt.broker.username != '':
            print('Com SENHA')
            print(publish.single(topico, valor,
                           hostname=self.atuador.mqtt.broker.endereco,
                           port=int(self.atuador.mqtt.broker.porta),
                           auth= {'username': self.atuador.mqtt.broker.username, 'password': self.atuador.mqtt.broker.password}))
        else:
            print('SEM SENHA')
            publish.single(topico, valor,
                           hostname=self.atuador.mqtt.broker.endereco,
                           port=int(self.atuador.mqtt.broker.porta))


class Atuador_boolean(Task):
    estado = models.NullBooleanField(default=False)
    atuador = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    def start(self, payload, dipo_pk):
        if self.atuador is not None and self.estado is not None:
            self.envia_mqtt(self.atuador.mqtt.topico, self.estado)
        if self.task_sucessor is not None:
            self.task_sucessor.start(payload, dipo_pk)

    def envia_mqtt(self, topico, valor):
        import paho.mqtt.publish as publish
        if self.atuador.mqtt.broker.username != '':
            publish.single(topico, valor,
                           hostname=self.atuador.mqtt.broker.endereco,
                           port=int(self.atuador.mqtt.broker.porta),
                           auth={'username': self.atuador.mqtt.broker.username, 'password': self.atuador.mqtt.broker.password})
        else:
            publish.single(topico, valor,
                           hostname=self.atuador.mqtt.broker.endereco,
                           port=int(self.atuador.mqtt.broker.porta))
