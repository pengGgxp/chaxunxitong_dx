# Generated by Django 5.0.1 on 2024-01-29 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0016_alter_days_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.DateTimeField(default=datetime.datetime(2004, 3, 21, 2, 0, 30), verbose_name='设置时间'),
        ),
    ]