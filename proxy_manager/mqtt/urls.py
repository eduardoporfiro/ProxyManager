from django.urls import path, include
from rest_framework import routers
from mqtt import views

router = routers.DefaultRouter()
router.register('broker', views.BrokerViewSet)
router.register('dado', views.DadoViewSet)
router.register('mqtt', views.MqttViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]