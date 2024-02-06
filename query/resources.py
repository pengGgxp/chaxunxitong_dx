from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import xuexiaoinfo, zhaoshengxinxi_danzhao, days, fenshuxianchaxun


class XuexiaoInfoResource(resources.ModelResource):
    xuexiaomingcheng = fields.Field(
        column_name='学校名称',
        attribute='xuexiaomingcheng',
    )
    xuexiaobiaoshima = fields.Field(
        column_name='学校标识码',
        attribute='xuexiaobiaoshima',
    )
    zhuguanbumen = fields.Field(
        column_name='主管部门',
        attribute='zhuguanbumen',
    )
    suozaidi = fields.Field(
        column_name='所在地',
        attribute='suozaidi',
    )
    banxuecengci = fields.Field(
        column_name='办学层次',
        attribute='banxuecengci',
    )
    beizhu = fields.Field(
        column_name='备注',
        attribute='beizhu',
    )

    class Meta:
        model = xuexiaoinfo


class ZhaoshengXinxi_DanZhaoResource(resources.ModelResource):
    xuexiaomingcheng = fields.Field(
        column_name='院校名称',
        attribute='xuexiaomingcheng',
        widget=ForeignKeyWidget(xuexiaoinfo, 'xuexiaomingcheng')
    )
    zhuanyemingcheng = fields.Field(
        column_name='专业名称',
        attribute='zhuanyemingcheng',
    )
    zhaoshengjihua = fields.Field(
        column_name='招生计划',
        attribute='zhaoshengjihua',
    )
    xuefei = fields.Field(
        column_name='学费',
        attribute='xuefei',
    )
    zhaoshengleixing = fields.Field(
        column_name='招生类型',
        attribute='zhaoshengleixing',
    )
    xingzhi = fields.Field(
        column_name='性质',
        attribute='xingzhi',
    )
    nianfen = fields.Field(
        column_name='年份',
        attribute='nianfen',
    )
    zhuanyeleibie = fields.Field(
        column_name='类别',
        attribute='zhuanyeleibie',
    )
    kebaozhiyuansl = fields.Field(
        column_name='可报志愿数量',
        attribute='kebaozhiyuansl',
    )
    kaoshineirong = fields.Field(
        column_name='考试内容',
        attribute='kaoshineirong',
    )

    kaoshifangshi = fields.Field(
        column_name='考试方式',
        attribute='kaoshifangshi',
    )

    class Meta:
        model = zhaoshengxinxi_danzhao


class DaysResource(resources.ModelResource):
    class Meta:
        model = days


class fenshuxianchaxunResource(resources.ModelResource):
    xuexiaomingcheng = fields.Field(
        column_name='院校名称',
        attribute='xuexiaomingcheng',
        widget=ForeignKeyWidget(xuexiaoinfo, 'xuexiaomingcheng')
    )
    zhuanyeleibie = fields.Field(
        column_name='专业类别',
        attribute='zhuanyeleibie',
    )
    zhaoshengzhuanye = fields.Field(
        column_name='招生专业',
        attribute='zhaoshengzhuanye',
    )
    zuidifenshu = fields.Field(
        column_name='最低分数',
        attribute='zuidifenshu',
    )
    zuidiweici = fields.Field(
        column_name='最低位次',
        attribute='zuidiweici',
    )
    benkezigexian = fields.Field(
        column_name='本科资格线',
        attribute='benkezigexian',
    )

    zhuankezigexian = fields.Field(
        column_name='专科资格线',
        attribute='zhuankezigexian',
    )

    nianfen = fields.Field(
        column_name='年份',
        attribute='nianfen',
    )

    class Meta:
        model = fenshuxianchaxun
