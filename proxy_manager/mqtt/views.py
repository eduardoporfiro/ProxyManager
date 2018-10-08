from mqtt.models import Broker, Dado, Mqtt, Dispositivo, Dado
from rest_framework import generics, mixins
from mqtt.serializers import BrokerSerializer, MqttSerializer, DispositivoSerializer, DadoSerializer


class BrokerUpdate (generics.UpdateAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer
    lookup_field = 'id'


class BrokerList(generics.ListAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer


class DadoList(generics.ListAPIView):
    queryset = Dado.objects.all()
    serializer_class = DadoSerializer


class MqttList(generics.ListCreateAPIView):
    queryset = Mqtt.objects.all()
    serializer_class = MqttSerializer
    filter_fields = ('topico', 'RC', 'QoS')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MqttUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mqtt.objects.all()
    serializer_class = MqttSerializer
    lookup_field = 'id'


class DispositivoList(generics.ListCreateAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    filter_fields = ('nome', 'tipo', 'mqtt')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DispositivoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    lookup_field = 'id'