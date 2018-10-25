# Generated by Django 2.0.5 on 2018-10-25 01:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mqtt', '0007_auto_20181020_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QoS', models.IntegerField(choices=[(0, 'QoS - 0'), (1, 'QoS - 1'), (2, 'QoS - 2')], default=0, editable=False)),
                ('valor_char', models.CharField(blank=True, max_length=500)),
                ('valor_int', models.IntegerField(blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.IntegerField(choices=[(0, 'Atuador'), (1, 'Sensor')], default=0)),
                ('is_int', models.BooleanField(default=False)),
                ('mqtt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dispositivo', to='mqtt.Mqtt')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workspace', models.TextField()),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('dispositivo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='tarefa.Dispositivo')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(0, 'save_database'), (1, 'dado_sensor_numero'), (2, 'dado_sensor_string'), (3, 'dados_sensor_media'), (4, 'dado_sensor_min'), (5, 'dado_sensor_max'), (6, 'if_sensor_string'), (7, 'if_sensor_numero'), (8, 'if_sensor_boolean'), (9, 'if_sensor_dadosensor'), (10, 'atuador_troca_estado'), (11, 'atuador_boolean')], default=0)),
                ('comando', models.CharField(max_length=200)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Atuador_boolean',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tarefa.Task')),
                ('estado', models.NullBooleanField()),
                ('atuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.Dispositivo')),
            ],
            bases=('tarefa.task',),
        ),
        migrations.CreateModel(
            name='Atuador_troca_estado',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tarefa.Task')),
                ('estado_anterior', models.NullBooleanField()),
                ('estado_atual', models.NullBooleanField()),
                ('atuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.Dispositivo')),
            ],
            bases=('tarefa.task',),
        ),
        migrations.CreateModel(
            name='If_sensor_boolean',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tarefa.Task')),
                ('condicao', models.IntegerField(choices=[(0, '='), (1, '!=')])),
                ('valor', models.NullBooleanField()),
            ],
            bases=('tarefa.task',),
        ),
        migrations.CreateModel(
            name='If_sensor_dadosensor',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tarefa.Task')),
                ('condicao', models.IntegerField(choices=[(0, '='), (1, '!='), (2, '>'), (3, '>='), (4, '<'), (5, '<=')])),
            ],
            bases=('tarefa.task',),
        ),
        migrations.CreateModel(
            name='If_sensor_numero',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tarefa.Task')),
                ('condicao', models.IntegerField(choices=[(0, '='), (1, '!='), (2, '>'), (3, '>='), (4, '<'), (5, '<=')])),
                ('valor', models.IntegerField()),
            ],
            bases=('tarefa.task',),
        ),
        migrations.CreateModel(
            name='If_sensor_string',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tarefa.Task')),
                ('condicao', models.IntegerField(choices=[(0, '='), (1, '!=')])),
                ('valor', models.CharField(max_length=200)),
            ],
            bases=('tarefa.task',),
        ),
        migrations.AddField(
            model_name='task',
            name='task_anterior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anterior', to='tarefa.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_sucessor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sucessor', to='tarefa.Task'),
        ),
        migrations.AddField(
            model_name='job',
            name='firs_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.Task'),
        ),
        migrations.AddField(
            model_name='dado',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.Dispositivo'),
        ),
        migrations.AddField(
            model_name='if_sensor_dadosensor',
            name='valor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='If_sensor_dadosensor', to='tarefa.Task'),
        ),
    ]
