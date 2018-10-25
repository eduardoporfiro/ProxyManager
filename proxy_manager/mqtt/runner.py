import paho.mqtt.client as mqtt
from mqtt.models import Mqtt, Broker
from tarefa.models import Dado, Dispositivo
topico =0

def on_connect(client, userdata, flags, rc):
    mqtt = Mqtt.objects.all().filter(broker_id=1).first()
    client.subscribe(topico)

def on_message(client, userdata, msg):
    if(msg.topic == 'proxy/parar'):
        broker = Broker.objects.get(pk=1)
        print('parando')
        broker.estado = 5
        broker.save()
    else:
        mqtt = Mqtt.objects.get(topico=msg.topic)
        if(mqtt != None):
            if(mqtt.dispositivo.is_int):
                dado = Dado(sensor=mqtt.dispositivo,  valor_int=int(msg.payload.decode('UTF-8')))
            else:
                dado = Dado(sensor=mqtt.dispositivo, valor_char=str(msg.payload.decode('UTF-8')))
            dado.save()
        print(msg.topic+" -  "+str(msg.payload))

def on_disconnect(client, userdata, rc):
    client.loop_stop(force=False)
    mqtt = Mqtt.objects.all().filter(broker_id=1).first()
    mqtt.RC = rc
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")

def start():
    client = mqtt.Client()
    broker = Broker.objects.get(pk=1)
    if (broker != None):
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