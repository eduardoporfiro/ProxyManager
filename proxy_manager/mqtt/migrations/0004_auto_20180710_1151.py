# Generated by Django 2.0.5 on 2018-07-10 14:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0003_auto_20180710_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dado',
            name='QoS',
            field=models.IntegerField(choices=[(0, 'QoS - 0'), (1, 'QoS - 1'), (2, 'QoS - 2')], editable=False),
        ),
        migrations.AlterField(
            model_name='dado',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 10, 14, 51, 2, 476494, tzinfo=utc)),
        ),
    ]