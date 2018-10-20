from rest_framework import generics, mixins
from tarefas.models import Dispositivo, Dado
from tarefas.serializers import DispositivoSerializer, DadoSerializer

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
