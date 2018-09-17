# Generated by Django 2.0.5 on 2018-07-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0012_auto_20180710_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='estado',
            field=models.IntegerField(choices=[(0, 'Desligado'), (1, 'Iniciando'), (2, 'Rodando'), (3, 'Com Problemas'), (4, 'Não Conectado'), (5, 'Parando')], default=0),
        ),
    ]