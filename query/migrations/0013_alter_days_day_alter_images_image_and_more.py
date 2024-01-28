# Generated by Django 5.0.1 on 2024-01-28 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0012_images_alter_days_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 28, 9, 14, 26, 337066), verbose_name='设置时间'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='imgs/admin/', verbose_name='路径'),
        ),
        migrations.AlterField(
            model_name='images',
            name='is_logo',
            field=models.BooleanField(default=False, verbose_name='LOGO'),
        ),
        migrations.AlterField(
            model_name='images',
            name='is_watermark',
            field=models.BooleanField(default=False, verbose_name='水印'),
        ),
    ]
