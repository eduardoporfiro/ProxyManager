from django.contrib import admin
from tarefas.models import Dado, Dispositivo, Atuador_troca_estado, Atuador_boolean, Task, Job

admin.site.register(Dispositivo)
admin.site.register(Dado)
admin.site.register(Job)
admin.site.register(Atuador_troca_estado)
admin.site.register(Atuador_boolean)

