import paho.mqtt.client as mqtt
from mqtt.models import Dado, Mqtt, Broker
topico =0
pk = 0
def on_connect(client, userdata, flags, rc):
    client.subscribe(topico)

def on_message(client, userdata, msg):
    if(msg.topic == 'proxy/parar'):
        broker = Broker.objects.all().filter(id=pk).first()
        print('parando')
        broker.estado = 5
        broker.save()
    else:
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

def start():
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
            print("Iniciei")
            broker.estado=2 #rodando
            broker.save()
        except:
            print("erro")
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