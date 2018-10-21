from django.urls import path
from tarefas import views

urlpatterns = [
    path('dispositivo/', views.DispositivoList.as_view(), name='dispositivo_list'),
    path('<int:id>/dispositivoUpdate/', views.DispositivoUpdateDelete.as_view(), name='dispositivo_update'),

    path('task/', views.TaskList.as_view(), name='task_list'),
    path('<int:id>/taskUpdate/', views.TaskUpdateDelete.as_view(), name='task_update'),

    path('atuador_troca_estado/', views.Atuador_booleanList.as_view(), name='atuador_troca_estado'),
    path('<int:id>/atuador_troca_estadoUpdate/', views.Atuador_troca_estadoUpdateDelete.as_view(),
         name='atuador_troca_estado_update'),

    path('atuador_boolean/', views.Atuador_booleanList.as_view(), name='atuador_boolean'),
    path('<int:id>/atuador_booleanUpdate/', views.Atuador_troca_estadoUpdateDelete.as_view(),
         name='atuador_boolean_update'),

    path('if_sensor_numero/', views.If_sensor_numeroList.as_view(), name='if_sensor_numero'),
    path('<int:id>/if_sensor_numero/', views.If_sensor_numeroUpdateDelete.as_view(),
         name='if_sensor_numero_update'),

    path('if_sensor_string/', views.If_sensor_stringList.as_view(), name='if_sensor_string'),
    path('<int:id>/if_sensor_string/', views.If_sensor_stringUpdateDelete.as_view(),
         name='if_sensor_string_update'),

    path('if_sensor_dadosensor/', views.If_sensor_dadosensorList.as_view(), name='if_sensor_dadosensor'),
    path('<int:id>/if_sensor_dadosensor/', views.If_sensor_dadosensorUpdateDelete.as_view(),
         name='if_sensor_dadosensor_update'),

    path('if_sensor_boolean/', views.If_sensor_booleanList.as_view(), name='if_sensor_boolean'),
    path('<int:id>/if_sensor_boolean/', views.If_sensor_booleanUpdateDelete.as_view(),
         name='if_sensor_boolean_update'),

    path('job/', views.JobList.as_view(), name='job'),
    path('<int:id>/job/', views.JobUpdateDelete.as_view(),
         name='job_update'),

    path('dado/', views.DadoList.as_view(), name='dadolist'),
]