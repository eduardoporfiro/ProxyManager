from django.contrib import admin
from tarefa.models import *

admin.site.register(Dispositivo)
admin.site.register(Dado)
admin.site.register(Job)
admin.site.register(Atuador_troca_estado)
admin.site.register(Atuador_boolean)
admin.site.register(Task)
admin.site.register(If_sensor_numero)
admin.site.register(If_sensor_string)
admin.site.register(If_sensor_dadosensor)
admin.site.register(If_sensor_boolean)

admin.site.register(If_else_sensor_boolean)
admin.site.register(If_else_sensor_dadosensor)
admin.site.register(If_else_sensor_numero)
admin.site.register(If_else_sensor_string)

