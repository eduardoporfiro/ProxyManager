from rest_framework import serializers
from mqtt.models import Broker, Dado, Mqtt

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = '__all__'

class DadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dado
        fields = '__all__'

class MqttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mqtt
        exclude =[
            'RC',
        ]