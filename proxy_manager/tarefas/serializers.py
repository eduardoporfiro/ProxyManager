from rest_framework import serializers
from tarefas.models import Dispositivo, Dado
from core.models import Task,Atuador_troca_estado, Atuador_boolean,\
    If_sensor_string,If_sensor_numero, If_sensor_dadosensor


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