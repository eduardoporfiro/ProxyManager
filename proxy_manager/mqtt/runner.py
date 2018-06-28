import paho.mqtt.client as mqtt
from mqtt.models import Dado, Mqtt, Broker
topico =0

def on_connect(client, userdata, flags, rc):
    client.subscribe(topico)

def on_message(client, userdata, msg):
    mqtt = Mqtt.objects.all().filter(topico=msg.topic).first()
    if(mqtt != None):
        dado = Dado(mqtt=mqtt, dado=str(msg.payload))
        dado.save()
    print(msg.topic+" -  "+str(msg.payload))

def on_disconnect(client, userdata, rc):
    client.loop_stop(force=False)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")

def start(pk):
    client = mqtt.Client()
    broker = Broker.objects.all().filter(pk=pk).first()
    if (broker != None):
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_disconnect = on_disconnect
        print(broker.endereco)
        # Conecta no MQTT Broker, no meu caso, o Mosquitto
        try:
            client.connect(broker.endereco, int(broker.porta), 60)
        except:
            broker.ESTADO_BROKER = 'off'
            broker.save()
            pass
        while broker.estado == 0:
            client.loop_start()
            broker.ESTADO_BROKER = 1
            broker.save()
            broker.refresh_from_db()
        print("Refresh")
        client.disconnect()
        broker.ESTADO_BROKER = 0
        broker.save()
        print("desliguei")
    else:
        print("Sem Broker")