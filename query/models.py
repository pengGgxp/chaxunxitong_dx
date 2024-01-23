import datetime

from django.db import models


# Create your models here.
class xuexiaoinfo(models.Model):
    # xuexiaomingcheng = models.CharField(verbose_name='学校名称', max_length=200)
    xuexiaomingcheng = models.CharField(verbose_name='学校名称', max_length=200)
    xuexiaobiaoshima = models.IntegerField(verbose_name='学校标识码', default=4111010001)
    zhuguanbumen = models.CharField(verbose_name='主管部门', max_length=200)
    suozaidi = models.CharField(verbose_name='所在地', max_length=200)

    BANXUECENGCI_CHOICES = [
        ('本科', '本科'),
        ('专科', '专科'),
    ]

    bianxuecengci = models.CharField(verbose_name='办学层次', choices=BANXUECENGCI_CHOICES, max_length=200)
    BEIZHU_CHOICES = [
        ('公办', '公办'),
        ('民办', '民办'),
        ('中外合作办学', '中外合作办学'),
        ('内地与港澳台地区合作办学', '内地与港澳台地区合作办学'),
    ]
    beizhu = models.CharField(verbose_name='备注', max_length=200, choices=BEIZHU_CHOICES)

    def __str__(self):
        return self.xuexiaomingcheng

    class Meta:
        verbose_name = '学校信息'
        verbose_name_plural = '学校信息'


class zhaoshengxinxi(models.Model):
    xuexiaomingcheng = models.ForeignKey(xuexiaoinfo, on_delete=models.CASCADE, verbose_name='学校名称')
    zhuanyemingcheng = models.CharField(verbose_name='专业名称', max_length=200)
    zhaoshengjihua = models.IntegerField(verbose_name='招生计划')
    xuefei = models.FloatField(verbose_name='学费')
    zhaoshengleixing = models.CharField(verbose_name='招生类型', max_length=200)
    XINGZHI_CHOICES = [
        ('本科', '本科'),
        ('专科', '专科'),
    ]
    xingzhi = models.CharField(verbose_name='性质（专科/本科）', max_length=200, choices=XINGZHI_CHOICES)
    nianfen = models.IntegerField(verbose_name='年份', default=datetime.datetime.now().year)
    zhuanyeleibie = models.CharField(verbose_name='专业类别', max_length=200)
    kebaozhiyuansl = models.IntegerField(verbose_name='可报志愿数量')
    kaoshineirong = models.TextField(verbose_name='考试内容')
    KAOSHIFANGSHI_CHOICES = [
        ('线上', '线上'),
        ('线下', '线下'),
    ]
    kaoshifangshi = models.CharField(verbose_name='考试方式', max_length=200, choices=KAOSHIFANGSHI_CHOICES, default='线下')

    class Meta:
        verbose_name = '招生信息'
        verbose_name_plural = '招生信息'
