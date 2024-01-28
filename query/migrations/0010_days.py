# Generated by Django 5.0.1 on 2024-01-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0009_alter_xuexiaoinfo_beizhu'),
    ]

    operations = [
        migrations.CreateModel(
            name='days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(default=0, verbose_name='设置时间')),
                ('name', models.CharField(default='NEW', max_length=200, verbose_name='名字')),
                ('beizhu', models.TextField(default='这里是备注', null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '倒计时',
                'verbose_name_plural': '倒计时',
            },
        ),
    ]