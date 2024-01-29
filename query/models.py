import datetime

from django.db import models


# Create your models here.
class xuexiaoinfo(models.Model):
    # xuexiaomingcheng = models.CharField(verbose_name='学校名称', max_length=200)
    xuexiaomingcheng = models.CharField(verbose_name='学校名称', max_length=200)
    xuexiaobiaoshima = models.TextField(verbose_name='学校标识码', default='4111010001', null=True, blank=True)
    zhuguanbumen = models.CharField(verbose_name='主管部门', max_length=200, null=True, blank=True)
    suozaidi = models.CharField(verbose_name='所在地', max_length=200, null=True, blank=True)

    BANXUECENGCI_CHOICES = [
        ('本科', '本科'),
        ('专科', '专科'),
    ]

    banxuecengci = models.CharField(verbose_name='办学层次', choices=BANXUECENGCI_CHOICES, max_length=200, null=True,
                                    blank=True)
    BEIZHU_CHOICES = [
        ('公办', '公办'),
        ('民办', '民办'),
        ('中外合作办学', '中外合作办学'),
        ('内地与港澳台地区合作办学', '内地与港澳台地区合作办学'),
    ]
    beizhu = models.CharField(verbose_name='备注', max_length=200, choices=BEIZHU_CHOICES, null=True, blank=True,
                              default='公办')

    def __str__(self):
        return self.xuexiaomingcheng

    class Meta:
        verbose_name = '学校信息'
        verbose_name_plural = '学校信息'


class zhaoshengxinxi(models.Model):
    xuexiaomingcheng = models.ForeignKey(xuexiaoinfo, on_delete=models.CASCADE, verbose_name='学校名称', null=True,
                                         blank=True)
    zhuanyemingcheng = models.CharField(verbose_name='专业名称', max_length=200, null=True, blank=True)
    zhaoshengjihua = models.IntegerField(verbose_name='招生计划', null=True, blank=True)
    xuefei = models.FloatField(verbose_name='学费', null=True, blank=True)
    zhaoshengleixing = models.CharField(verbose_name='招生类型', max_length=200, null=True, blank=True)
    XINGZHI_CHOICES = [
        ('本科', '本科'),
        ('专科', '专科'),
    ]
    xingzhi = models.CharField(verbose_name='性质（专科/本科）', max_length=200, choices=XINGZHI_CHOICES, null=True,
                               blank=True)
    nianfen = models.IntegerField(verbose_name='年份', default=datetime.datetime.now().year, null=True, blank=True)
    zhuanyeleibie = models.CharField(verbose_name='专业类别', max_length=200, null=True, blank=True)
    kebaozhiyuansl = models.IntegerField(verbose_name='可报志愿数量', null=True, blank=True)
    kaoshineirong = models.TextField(verbose_name='考试内容', null=True, blank=True)
    KAOSHIFANGSHI_CHOICES = [
        ('线上', '线上'),
        ('线下', '线下'),
    ]
    kaoshifangshi = models.CharField(verbose_name='考试方式', max_length=200, choices=KAOSHIFANGSHI_CHOICES,
                                     default='线下', null=True, blank=True)

    class Meta:
        verbose_name = '招生信息'
        verbose_name_plural = '招生信息'


class days(models.Model):
    day = models.DateTimeField(verbose_name='设置时间', null=False, default=datetime.datetime(2004, 3, 21, 2, 0, 30))
    name = models.CharField(verbose_name='名字', null=False, default='NEW', max_length=200)
    beizhu = models.TextField(verbose_name='备注', null=True, default='这里是备注')

    class Meta:
        verbose_name = '倒计时'
        verbose_name_plural = '倒计时'


class Images(models.Model):
    image = models.ImageField(upload_to='imgs/admin/', verbose_name='路径')
    is_logo = models.BooleanField(default=False, verbose_name='LOGO')
    is_watermark = models.BooleanField(default=False, verbose_name='水印')


    class Meta:
        verbose_name = '图片功能'
        verbose_name_plural = '图片功能'
