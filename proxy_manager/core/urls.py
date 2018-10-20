from django.urls import path, include
from core import views
from rest_framework.authtoken import views as views_rest

urlpatterns = [
    path('', views.home, name='broker_list'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views_rest.obtain_auth_token)
]