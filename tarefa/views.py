from rest_framework import generics, mixins
from tarefa.models import Dispositivo, Dado
from tarefa.serializers import *

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


class DadoList(generics.ListAPIView):
    queryset = Dado.objects.all()
    serializer_class = DadoSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class Atuador_troca_estadoList(generics.ListCreateAPIView):
    queryset = Atuador_troca_estado.objects.all()
    serializer_class = Atuador_troca_estadoSerializer


class Atuador_troca_estadoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atuador_troca_estado.objects.all()
    serializer_class = Atuador_troca_estadoSerializer
    lookup_field = 'id'


class Atuador_booleanList(generics.ListCreateAPIView):
    queryset = Atuador_boolean.objects.all()
    serializer_class = Atuador_booleanSerializer


class Atuador_booleanUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atuador_boolean.objects.all()
    serializer_class = Atuador_booleanSerializer
    lookup_field = 'id'


class If_sensor_stringList(generics.ListCreateAPIView):
    queryset = If_sensor_string.objects.all()
    serializer_class = If_sensor_stringSerializer


class If_sensor_stringUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = If_sensor_string.objects.all()
    serializer_class = If_sensor_stringSerializer
    lookup_field = 'id'


class If_sensor_numeroList(generics.ListCreateAPIView):
    queryset = If_sensor_numero.objects.all()
    serializer_class = If_sensor_numeroSerializer


class If_sensor_numeroUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = If_sensor_numero.objects.all()
    serializer_class = If_sensor_numeroSerializer
    lookup_field = 'id'

class If_sensor_dadosensorList(generics.ListCreateAPIView):
    queryset = If_sensor_dadosensor.objects.all()
    serializer_class = If_sensor_numeroSerializer


class If_sensor_dadosensorUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = If_sensor_dadosensor.objects.all()
    serializer_class = If_sensor_dadosensorSerializer
    lookup_field = 'id'


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_fields = ('id',)


class JobUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'


class If_sensor_booleanList(generics.ListCreateAPIView):
    queryset = If_sensor_boolean.objects.all()
    serializer_class = If_sensor_booleanSerializer


class If_sensor_booleanUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = If_sensor_boolean.objects.all()
    serializer_class = If_sensor_booleanSerializer
    lookup_field = 'id'
