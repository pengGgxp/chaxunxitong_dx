# Generated by Django 5.0.1 on 2024-01-29 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0015_alter_days_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 29, 8, 54, 28, 14865), verbose_name='设置时间'),
        ),
    ]
