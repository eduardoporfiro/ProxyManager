from django.contrib import admin
from mqtt.models import Broker, Mqtt
admin.site.register(Broker)
admin.site.register(Mqtt)
