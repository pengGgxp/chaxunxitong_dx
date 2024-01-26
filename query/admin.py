from django.contrib import admin
from import_export.admin import ExportMixin, ImportExportModelAdmin

from query.models import xuexiaoinfo, zhaoshengxinxi, days
from query.resources import XuexiaoInfoResource, ZhaoshengXinxiResource, DaysResource


# Register your models here.

class XuexiaoinfoAdmin(ImportExportModelAdmin):
    list_display = ('xuexiaomingcheng', 'xuexiaobiaoshima', 'zhuguanbumen', 'suozaidi', 'banxuecengci', 'beizhu')
    search_fields = ['xuexiaomingcheng']
    resource_class = XuexiaoInfoResource


admin.site.register(xuexiaoinfo, XuexiaoinfoAdmin)


class ZhaoshengxinxiAdmin(ImportExportModelAdmin):
    list_display = (
        'xuexiaomingcheng', 'zhuanyemingcheng', 'zhaoshengjihua', 'xuefei', 'zhaoshengleixing', 'xingzhi', 'nianfen',
        'zhuanyeleibie', 'kebaozhiyuansl', 'kaoshineirong', 'kaoshifangshi')
    list_filter = ('xuexiaomingcheng', 'zhaoshengleixing', 'xingzhi', 'nianfen', 'zhuanyeleibie', 'kaoshifangshi')
    resource_class = ZhaoshengXinxiResource
    autocomplete_fields = ['xuexiaomingcheng']


admin.site.register(zhaoshengxinxi, ZhaoshengxinxiAdmin)

class DaysAdmin(ImportExportModelAdmin):
    list_display = (
        'day','name','beizhu'
    )
    resource_class = DaysResource

admin.site.register(days,DaysAdmin)