# Generated by Django 2.0.5 on 2018-10-08 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0005_dado_is_int'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dado',
            name='is_int',
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='is_int',
            field=models.BooleanField(default=False),
        ),
    ]
