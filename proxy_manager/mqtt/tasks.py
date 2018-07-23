from __future__ import absolute_import, unicode_literals
from proxy_manager.celery import app
from mqtt.models import Broker, Mqtt
from mqtt import runner as conect
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def start():
    for broker in Broker.objects.all():
        if (broker.estado == 0):
            iniciar(broker)
@app.task
def restart():
    for broker in Broker.objects.all():
        if(broker.estado == 4):#se estiver sem conexão ou parando
            iniciar(broker)

#função padrão para iniciar ou reiniciar
def iniciar(broker):
    topicos =[('proxy/parar', 0)]
    for mqtts in Mqtt.objects.all().filter(broker=broker):
        topicos.append((mqtts.topico, mqtts.QoS))
    conect.topico = topicos
    conect.pk = broker.pk
    broker.estado = 1  # iniciando
    broker.save()
    conect.start()