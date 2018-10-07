from django.urls import path, include
from core import views
urlpatterns = [
    path('', views.home, name='broker_list'),
]