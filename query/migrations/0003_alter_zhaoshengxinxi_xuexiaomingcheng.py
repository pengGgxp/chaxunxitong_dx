# Generated by Django 5.0.1 on 2024-01-22 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_alter_zhaoshengxinxi_xingzhi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhaoshengxinxi',
            name='xuexiaomingcheng',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.xuexiaoinfo', verbose_name='学校名称'),
        ),
    ]
