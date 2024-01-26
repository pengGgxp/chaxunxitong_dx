from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import xuexiaoinfo,zhaoshengxinxi
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

    def dehydrate_beizhu(self, obj):
        # 检查 obj 的 beizhu 值，如果为空，替换成 '公办'
        return obj.beizhu if obj.beizhu else '公办'
    class Meta:
        model = xuexiaoinfo


class ZhaoshengXinxiResource(resources.ModelResource):
    xuexiaomingcheng = fields.Field(
        column_name='xuexiaomingcheng',
        attribute='xuexiaomingcheng',
        widget=ForeignKeyWidget(xuexiaoinfo, 'xuexiaomingcheng')
    )

    class Meta:
        model = zhaoshengxinxi
