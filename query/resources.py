from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import xuexiaoinfo, zhaoshengxinxi, days


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


class ZhaoshengXinxiResource(resources.ModelResource):
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
        model = zhaoshengxinxi


class DaysResource(resources.ModelResource):
    class Meta:
        model = days