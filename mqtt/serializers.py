from rest_framework import serializers
from mqtt.models import Broker, Mqtt

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = '__all__'


class MqttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mqtt
        exclude =[
            'RC',
        ]