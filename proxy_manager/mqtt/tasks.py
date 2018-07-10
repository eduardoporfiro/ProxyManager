from __future__ import absolute_import, unicode_literals
from celery import shared_task
from proxy_manager.celery import app
from mqtt.models import Broker, Mqtt
from mqtt import runner as conect
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def start():
    topicos =[]
    for broker in Broker.objects.all():
        if (broker.estado == 0):
            for mqtts in Mqtt.objects.all().filter(broker=broker):
                topicos.append((mqtts.topico, 0))
            conect.topico = topicos
            broker.estado=1 #iniciando
            broker.save()
            conect.start(broker.pk)