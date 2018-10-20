from django.urls import path, include
from mqtt import views


urlpatterns = [
    path('broker/', views.BrokerList.as_view(), name='broker_list'),
    path('brokerUpdate/<int:id>/', views.BrokerUpdate.as_view(), name='broker_update'),

    path('mqtt/', views.MqttList.as_view(), name='mqtt_list'),
    path('<int:id>/mqttUpdate/', views.MqttUpdateDelete.as_view(), name='mqtt_update'),
]