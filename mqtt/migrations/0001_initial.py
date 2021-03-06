# Generated by Django 2.0.5 on 2018-10-07 23:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=200)),
                ('porta', models.IntegerField(default=1883)),
                ('username', models.CharField(blank=True, max_length=200)),
                ('password', models.CharField(blank=True, max_length=200)),
                ('estado', models.IntegerField(choices=[(0, 'Desligado'), (1, 'Iniciando'), (2, 'Rodando'), (3, 'Com Problemas'), (4, 'Não Conectado'), (5, 'Parando')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mqtt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topico', models.CharField(max_length=250)),
                ('QoS', models.IntegerField(choices=[(0, 'QoS - 0'), (1, 'QoS - 1'), (2, 'QoS - 2')], default=0)),
                ('RC', models.IntegerField(choices=[(0, 'Conexão Aceita'), (1, 'Conexão Recusada, Versão de Protocolo não aceita'), (2, 'Conexão Recusada, identificador recusado'), (3, 'Conexão Recusada, servidor indisponível'), (4, 'Conexão Recusada, Usuário ou Senha inválido'), (5, 'Conexão Recusada, conexão não autorizada')], default=0)),
                ('broker', models.ForeignKey(on_delete=True, to='mqtt.Broker')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='mqtt',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='mqtt.Mqtt'),
        ),
        migrations.AddField(
            model_name='dado',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mqtt.Dispositivo'),
        ),
    ]
