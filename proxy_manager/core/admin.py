from .models import *
from django.contrib import admin

admin.site.register(Celery)
admin.site.register(Task)
admin.site.register(If_sensor_numero)
admin.site.register(If_sensor_string)
admin.site.register(If_sensor_dadosensor)
admin.site.register(If_sensor_boolean)
