from django.contrib import admin
from mqtt.models import Broker, Mqtt
from solo.admin import SingletonModelAdmin
admin.site.register(Broker, SingletonModelAdmin)
admin.site.register(Mqtt)