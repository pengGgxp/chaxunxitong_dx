from django.contrib import admin
from import_export.admin import ExportMixin, ImportExportModelAdmin

from query.models import xuexiaoinfo, zhaoshengxinxi_danzhao, days, Images, fenshuxianchaxun
from query.resources import XuexiaoInfoResource, ZhaoshengXinxi_DanZhaoResource, DaysResource, fenshuxianchaxunResource
from query.form import ImagesForm


# Register your models here.

class XuexiaoinfoAdmin(ImportExportModelAdmin):
    list_display = ('xuexiaomingcheng', 'xuexiaobiaoshima', 'zhuguanbumen', 'suozaidi', 'banxuecengci', 'beizhu')
    search_fields = ['xuexiaomingcheng']
    resource_class = XuexiaoInfoResource


admin.site.register(xuexiaoinfo, XuexiaoinfoAdmin)


class Zhaoshengxinxi_danzhaoAdmin(ImportExportModelAdmin):
    list_display = (
        'xuexiaomingcheng', 'zhuanyemingcheng', 'zhaoshengjihua', 'xuefei', 'zhaoshengleixing', 'xingzhi', 'nianfen',
        'zhuanyeleibie', 'kebaozhiyuansl', 'kaoshineirong', 'kaoshifangshi')
    list_filter = ('xuexiaomingcheng', 'zhaoshengleixing', 'xingzhi', 'nianfen', 'zhuanyeleibie', 'kaoshifangshi')
    resource_class = ZhaoshengXinxi_DanZhaoResource
    autocomplete_fields = ['xuexiaomingcheng']


admin.site.register(zhaoshengxinxi_danzhao, Zhaoshengxinxi_danzhaoAdmin)


class DaysAdmin(ImportExportModelAdmin):
    list_display = (
        'day', 'name', 'beizhu'
    )
    resource_class = DaysResource


admin.site.register(days, DaysAdmin)


class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'image', 'is_logo', 'is_watermark'
    )
    form = ImagesForm


admin.site.register(Images, ImagesAdmin)


class fenshuxianchaxunAdmin(ImportExportModelAdmin):
    list_display = (
        'xuexiaomingcheng', 'zhuanyeleibie', 'zhaoshengzhuanye', 'zuidifenshu', 'zuidiweici', 'benkezigexian',
        'zhuankezigexian', 'nianfen'
    )
    autocomplete_fields = ['xuexiaomingcheng']
    resource_class = fenshuxianchaxunResource


admin.site.register(fenshuxianchaxun, fenshuxianchaxunAdmin)
