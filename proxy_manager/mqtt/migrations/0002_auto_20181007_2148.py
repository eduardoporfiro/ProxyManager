# Generated by Django 2.0.5 on 2018-10-08 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='mqtt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mqtt.Mqtt'),
        ),
    ]
