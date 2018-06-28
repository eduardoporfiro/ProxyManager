from django.contrib import admin
from mqtt.models import Broker, Mqtt, Dado
admin.site.register(Broker)
admin.site.register(Mqtt)
admin.site.register(Dado)
