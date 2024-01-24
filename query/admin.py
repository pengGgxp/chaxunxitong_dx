from django.contrib import admin

from query.models import xuexiaoinfo, zhaoshengxinxi


# Register your models here.

class XuexiaoinfoAdmin(admin.ModelAdmin):
    list_display = ('xuexiaomingcheng', 'xuexiaobiaoshima', 'zhuguanbumen', 'suozaidi', 'bianxuecengci','beizhu')
    search_fields = ['xuexiaomingcheng']

admin.site.register(xuexiaoinfo, XuexiaoinfoAdmin)


class ZhaoshengxinxiAdmin(admin.ModelAdmin):
    list_display = (
    'xuexiaomingcheng', 'zhuanyemingcheng', 'zhaoshengjihua', 'xuefei', 'zhaoshengleixing', 'xingzhi', 'nianfen',
    'zhuanyeleibie', 'kebaozhiyuansl', 'kaoshineirong','kaoshifangshi')
    list_filter = ('xuexiaomingcheng', 'zhaoshengleixing', 'xingzhi', 'nianfen', 'zhuanyeleibie','kaoshifangshi')

    autocomplete_fields = ['xuexiaomingcheng']

admin.site.register(zhaoshengxinxi, ZhaoshengxinxiAdmin)
