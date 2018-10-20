from rest_framework import serializers
from tarefas.models import Dispositivo, Dado

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class DadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dado
        fields = '__all__'
