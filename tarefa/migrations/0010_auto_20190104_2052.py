# Generated by Django 2.1.4 on 2019-01-04 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0009_auto_20190104_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atuador_troca_estado',
            name='estado_anterior',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='atuador_troca_estado',
            name='estado_atual',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
