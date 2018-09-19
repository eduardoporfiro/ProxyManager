from django.urls import path, include
from rest_framework.authtoken import views as views_rest
from mqtt import views


urlpatterns = [
    path('broker/', views.BrokerList.as_view(), name='broker_list'),
    path('brokerUpdate/<int:id>/', views.BrokerUpdate.as_view(), name='broker_update'),

    path('mqtt/', views.MqttList.as_view(), name='mqtt_list'),
    path('<int:id>/mqttUpdate/', views.MqttUpdateDelete.as_view(), name='mqtt_update'),

    path('dado/', views.DadoList.as_view(), name='dadolist'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views_rest.obtain_auth_token)
]