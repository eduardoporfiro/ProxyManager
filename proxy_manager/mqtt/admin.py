from django.contrib import admin
from mqtt.models import Broker, Mqtt, Dado, Dispositivo
from solo.admin import SingletonModelAdmin
admin.site.register(Broker, SingletonModelAdmin)
admin.site.register(Mqtt)
admin.site.register(Dado)
admin.site.register(Dispositivo)
