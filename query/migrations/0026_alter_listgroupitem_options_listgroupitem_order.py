# Generated by Django 5.0.1 on 2024-02-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0025_listgroupitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listgroupitem',
            options={'ordering': ['order'], 'verbose_name': '首页跳转列表', 'verbose_name_plural': '首页跳转列表'},
        ),
        migrations.AddField(
            model_name='listgroupitem',
            name='order',
            field=models.IntegerField(default=0, verbose_name='排序顺序'),
        ),
    ]
