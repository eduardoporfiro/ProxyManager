from django.urls import path
from tarefas import views

urlpatterns = [
    path('dispositivo/', views.DispositivoList.as_view(), name='dispositivo_list'),
    path('<int:id>/dispositivoUpdate/', views.DispositivoUpdateDelete.as_view(), name='dispositivo_update'),

    path('dado/', views.DadoList.as_view(), name='dadolist'),
]