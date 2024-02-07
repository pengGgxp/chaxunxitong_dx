# Generated by Django 5.0.1 on 2024-02-07 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0024_alter_fenshuxianchaxun_benkezigexian_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListGroupItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('href', models.TextField(verbose_name='链接')),
                ('view_count', models.IntegerField(default=0, verbose_name='访问量')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.images', verbose_name='图片')),
            ],
            options={
                'verbose_name': '首页跳转列表',
                'verbose_name_plural': '首页跳转列表',
            },
        ),
    ]