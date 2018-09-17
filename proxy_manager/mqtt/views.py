from mqtt.models import Broker, Dado, Mqtt
from rest_framework import viewsets, mixins
from mqtt.serializers import BrokerSerializer, DadoSerializer, MqttSerializer

class BrokerViewSet(viewsets.ModelViewSet):
    queryset = Broker.objects.filter(pk=1).all()
    serializer_class = BrokerSerializer

class DadoViewSet(viewsets.ModelViewSet):
    queryset = Dado.objects.all()
    serializer_class = DadoSerializer

class MqttViewSet(viewsets.ModelViewSet):
    queryset = Mqtt.objects.all()
    serializer_class = MqttSerializer