# Generated by Django 2.0.5 on 2018-07-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0007_auto_20180710_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='estado',
            field=models.IntegerField(default=0),
        ),
    ]