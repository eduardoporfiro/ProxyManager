from rest_framework import serializers
from tarefa.models import *

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'


class DadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dado
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class Atuador_troca_estadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atuador_troca_estado
        fields = '__all__'


class Atuador_booleanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atuador_boolean
        fields = '__all__'


class If_sensor_stringSerializer(serializers.ModelSerializer):
    class Meta:
        model = If_sensor_string
        fields = '__all__'


class If_sensor_numeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = If_sensor_numero
        fields = '__all__'


class If_sensor_dadosensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = If_sensor_dadosensor
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class If_sensor_booleanSerializer(serializers.ModelSerializer):
    class Meta:
        model=If_sensor_boolean
        fields='__all__'