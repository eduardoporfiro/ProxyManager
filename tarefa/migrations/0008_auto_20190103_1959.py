# Generated by Django 2.1.3 on 2019-01-03 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0007_auto_20190103_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='if_else_sensor_boolean',
            name='elsetask',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elsetasksensor_boolean', to='tarefa.Task'),
        ),
        migrations.AlterField(
            model_name='if_else_sensor_dadosensor',
            name='elsetask',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elsetasksensor_dadosensor', to='tarefa.Task'),
        ),
        migrations.AlterField(
            model_name='if_else_sensor_numero',
            name='elsetask',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elsetasksensor_numero', to='tarefa.Task'),
        ),
    ]
