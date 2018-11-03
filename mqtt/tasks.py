from __future__ import absolute_import, unicode_literals
from proxy_manager.celery import app
from mqtt.models import Broker, Mqtt
from tarefa.models import *
from celery.utils.log import get_task_logger

import paho.mqtt.client as mqtt
from celery import group


logger = get_task_logger(__name__)
topico=[]


@app.task
def start():
    broker = Broker.objects.get(pk=1)
    if (broker.estado == 0):
        iniciar(broker)


@app.task
def restart():
    broker = Broker.objects.get(pk=1)
    if(broker.estado == 4):#se estiver sem conexão ou parando
        iniciar(broker)


#função padrão para iniciar ou reiniciar
def iniciar(broker):
    topico.append(('proxy/parar', 0))
    for mqtts in Mqtt.objects.all().filter(broker=broker):
        topico.append((mqtts.topico, mqtts.QoS))
    broker.estado = 1  # iniciando
    broker.save()
    iniciar_MQTT()


@app.task
def start_task(task_pk, payload, dispo_pk):
    task = Task.objects.get(pk=task_pk)
    print(payload)
    task.start(payload, dispo_pk)


def on_connect(client, userdata, flags, rc):
    client.subscribe(topico)


def on_message(client, userdata, msg):
    if msg.topic == 'proxy/parar':
        broker = Broker.objects.get(pk=1)
        print('parando')
        broker.estado = 5
        broker.save()
    else:
        mqtt = Mqtt.objects.filter(topico=msg.topic).exists()
        if mqtt != False:
            mqtt = Mqtt.objects.filter(topico=msg.topic).get()
            try:
                dispo = mqtt.dispositivo
                if dispo != None and dispo.tipo == 1:
                    start_task.delay(dispo.job.firs_task.pk, str(msg.payload.decode('UTF-8')), dispo.pk)
            except Exception as e:
                print(e)
        print(msg.topic+" -  "+str(msg.payload.decode('UTF-8')))


def on_disconnect(client, userdata, rc):
    client.loop_stop(force=False)
    mqtt = Mqtt.objects.all().filter(broker_id=1).first()
    mqtt.RC = rc
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")


def iniciar_MQTT():
    client = mqtt.Client()
    broker = Broker.objects.get(pk=1)
    if broker != None:
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_disconnect = on_disconnect
        # Conecta no MQTT Broker, no meu caso, o Mosquitto
        try:
            client.connect(broker.endereco, int(broker.porta), keepalive=10)
            print("Iniciei")
            broker.estado=2 #rodando
            broker.save()
        except:
            broker.estado = 4 #não conectado
            broker.save()
            return
        while broker.estado == 2:
            client.loop_start()
            broker.refresh_from_db()
        client.disconnect()
        print("desliguei")
    else:
        print("Sem Broker")