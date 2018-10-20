from mqtt.models import Broker,  Mqtt
from rest_framework import generics, mixins
from mqtt.serializers import BrokerSerializer, MqttSerializer


class BrokerUpdate (generics.UpdateAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer
    lookup_field = 'id'


class BrokerList(generics.ListAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer


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
