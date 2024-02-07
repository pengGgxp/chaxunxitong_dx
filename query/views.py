import encodings
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q, Count, F
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from django.views import View

from query.models import zhaoshengxinxi_danzhao, xuexiaoinfo, days, Images, fenshuxianchaxun, ListGroupItem


# Create your views here.
def index(request):
    logo_image = Images.objects.filter(is_logo=True).first()
    watermark_image = Images.objects.filter(is_watermark=True).first()
    listitem = ListGroupItem.objects.all()
    context = {
        'logo_image': logo_image,
        'watermark_image': watermark_image,
        'listitem': listitem,
    }
    return render(request, 'index.html', context=context)


def increase_view_count(request):
    list_group_item_id = request.POST.get('list_itemid')
    list_group_item = ListGroupItem.objects.get(id=list_group_item_id)
    list_group_item.increase_view_count()
    return JsonResponse({'jieguo': 'yes', 'href': list_group_item.href})


def cx_danzhao(request):
    logo_image = Images.objects.filter(is_logo=True).first()
    watermark_image = Images.objects.filter(is_watermark=True).first()
    context = {
        'leixing': zhaoshengxinxi_danzhao.objects.values_list('zhaoshengleixing', flat=True).distinct(),
        'nian': zhaoshengxinxi_danzhao.objects.values_list('nianfen', flat=True).distinct(),
        'banxuexingzhi': xuexiaoinfo.objects.values_list('beizhu', flat=True).distinct(),
        'fangshi': zhaoshengxinxi_danzhao.objects.values_list('kaoshifangshi', flat=True).distinct(),
        'logo_image': logo_image,
        'watermark_image': watermark_image,
    }

    return render(request, 'query/cx_danzhao.html', context=context)


class query_danzhao_processing(View):
    @staticmethod
    def post(request):
        querymode = request.POST.get('querymode')
        zhaoshengleixing = request.POST.get('zhaoshengleixing')
        nianfen = request.POST.get('nianfen')
        banxuexingzhi = request.POST.getlist('banxuexingzhi[]')
        kaoshifangshi = request.POST.getlist('kaoshifangshi[]')
        mingcheng = request.POST.get('mingcheng')

        result_data = {}
        queryset = zhaoshengxinxi_danzhao.objects.all()
        # queryset = zhaoshengxinxi_danzhao.objects.none()
        if querymode == 'xuexiao':
            if mingcheng:
                queryset = queryset.filter(xuexiaomingcheng__xuexiaomingcheng__icontains=mingcheng)
        if querymode == 'zhuanye':
            if mingcheng:
                queryset = queryset.filter(zhuanyemingcheng__icontains=mingcheng)

                queryset = queryset.values('xuexiaomingcheng__xuexiaomingcheng').annotate(count=Count('id'))
        if zhaoshengleixing:
            queryset = queryset.filter(zhaoshengleixing=zhaoshengleixing)
        if nianfen:
            queryset = queryset.filter(nianfen=nianfen)
        if banxuexingzhi:
            queryset = queryset.filter(xuexiaomingcheng__beizhu__in=banxuexingzhi)
        if kaoshifangshi:
            queryset = queryset.filter(kaoshifangshi__in=kaoshifangshi)
        result_data['querymode'] = querymode

        queryset = queryset.all().annotate(
            beizhu_xuexiaomingcheng=F('xuexiaomingcheng__beizhu'),
            xuexiaomingcheng_xuexiaomingcheng=F('xuexiaomingcheng__xuexiaomingcheng'),
        )
        tmp = list(queryset.all().values())

        # for entry in tmp:
        #     beizhu = xuexiaoinfo.objects.get(id=entry.get('xuexiaomingcheng_id')).beizhu
        #     xuexiaomingcheng = xuexiaoinfo.objects.get(id=entry.get('xuexiaomingcheng_id')).xuexiaomingcheng
        #     entry.update({'beizhu': beizhu, 'xuexiaomingcheng': xuexiaomingcheng})

        result_data['jieguo'] = json.dumps({'zhaoshengxinxi': tmp}, cls=DjangoJSONEncoder)
        if querymode == 'xuexiao':
            result = json.loads(result_data['jieguo'])

            new_dict = {}

            for entry in result['zhaoshengxinxi']:
                xuexiaomingcheng_id = entry['xuexiaomingcheng_id']

                if xuexiaomingcheng_id in new_dict:
                    new_dict[xuexiaomingcheng_id]['data'].append(entry)
                else:
                    new_dict[xuexiaomingcheng_id] = {
                        'xuexiaomingcheng_xuexiaomingcheng': entry['xuexiaomingcheng_xuexiaomingcheng'],
                        'beizhu_xuexiaomingcheng': entry['beizhu_xuexiaomingcheng'],
                        'kaoshifangshi': entry['kaoshifangshi'],
                        'kebaozhiyuansl': entry['kebaozhiyuansl'],
                        'kaoshineirong': entry['kaoshineirong'],
                        'data': [entry],
                    }
            return JsonResponse(new_dict)

        if querymode == 'zhuanye':
            result = json.loads(result_data['jieguo'])

            new_dict = {}
            for entry in result['zhaoshengxinxi']:
                zhuanyemingcheng = entry['zhuanyemingcheng']

                if zhuanyemingcheng in new_dict:
                    new_dict[zhuanyemingcheng]['data'].append(entry)
                else:
                    new_dict[zhuanyemingcheng] = {
                        'data': [entry],
                    }
            return JsonResponse(new_dict)


def daojishi(request):
    logo_image = Images.objects.filter(is_logo=True).first()
    watermark_image = Images.objects.filter(is_watermark=True).first()
    context = {
        'day': days.objects.all(),
        'logo_image': logo_image,
        'watermark_image': watermark_image,
    }
    return render(request, 'query/days.html', context=context)


def cx_benkefenshuxian(request):
    logo_image = Images.objects.filter(is_logo=True).first()
    watermark_image = Images.objects.filter(is_watermark=True).first()
    context = {
        'nian': fenshuxianchaxun.objects.values_list('nianfen', flat=True).distinct(),
        'banxuexingzhi': xuexiaoinfo.objects.values_list('beizhu', flat=True).distinct(),
        'zhuanyeleibie': fenshuxianchaxun.objects.values_list('zhuanyeleibie', flat=True).distinct(),
        'logo_image': logo_image,
        'watermark_image': watermark_image,
    }

    return render(request, 'query/cx_benkefenshuxian.html', context=context)


def cx_zhuankefenshuxian(request):
    logo_image = Images.objects.filter(is_logo=True).first()
    watermark_image = Images.objects.filter(is_watermark=True).first()
    context = {
        'nian': fenshuxianchaxun.objects.values_list('nianfen', flat=True).distinct(),
        'banxuexingzhi': xuexiaoinfo.objects.values_list('beizhu', flat=True).distinct(),
        'zhuanyeleibie': fenshuxianchaxun.objects.values_list('zhuanyeleibie', flat=True).distinct(),
        'logo_image': logo_image,
        'watermark_image': watermark_image,
    }

    return render(request, 'query/cx_zhuankefenshuxian.html', context=context)


class query_fenshuxian_processing(View):
    @staticmethod
    def post(request):
        querymode = request.POST.get('querymode')
        nianfen = request.POST.get('nianfen')
        banxuexingzhi = request.POST.getlist('banxuexingzhi[]')
        zhuanyeleibie = request.POST.get('zhuanyeleibie')
        fenshu = request.POST.get('fenshu')
        weici = request.POST.get('weici')
        mingcheng = request.POST.get('mingcheng')
        zhuan_ben = request.POST.get('zhuan_ben')

        result_data = {}
        queryset = fenshuxianchaxun.objects.all()
        if querymode == 'xuexiao':
            if mingcheng:
                queryset = queryset.filter(xuexiaomingcheng__xuexiaomingcheng__icontains=mingcheng)
        if querymode == 'zhuanye':
            if mingcheng:
                queryset = queryset.filter(zhaoshengzhuanye__icontains=mingcheng)
        if nianfen:
            queryset = queryset.filter(nianfen=nianfen)
        if zhuanyeleibie:
            queryset = queryset.filter(zhuanyeleibie=zhuanyeleibie)
        if fenshu:
            queryset = queryset.filter(zuidifenshu__lte=fenshu).order_by('-zuidifenshu')
        if weici:
            queryset = queryset.filter(zuidiweici__lte=weici).order_by('-zuidiweici')
        if zhuan_ben:
            queryset = queryset.filter(xuexiaomingcheng__banxuecengci=zhuan_ben)
        if banxuexingzhi:
            queryset = queryset.filter(xuexiaomingcheng__beizhu__in=banxuexingzhi)
        queryset = queryset.all().annotate(
            xuexiaomingcheng_xuexiaomingcheng=F('xuexiaomingcheng__xuexiaomingcheng'),
            beizhu_xuexiaomingcheng=F('xuexiaomingcheng__beizhu'),
        )
        result_data['jieguo'] = list(queryset.all().values())

        # print(json.dumps(result_data, indent=4))
        if querymode == 'xuexiao':
            new_dict = {}
            for entry in result_data['jieguo']:
                xuexiaomingcheng = entry['xuexiaomingcheng_xuexiaomingcheng']
                if xuexiaomingcheng in new_dict:
                    new_dict[xuexiaomingcheng]['data'].append(entry)
                else:
                    new_dict[xuexiaomingcheng] = {
                        'xuexiaomingcheng_xuexiaomingcheng': entry['xuexiaomingcheng_xuexiaomingcheng'],
                        'beizhu_xuexiaomingcheng': entry['beizhu_xuexiaomingcheng'],
                        'data': [entry],
                    }
                    # if zhuan_ben == '本科':
                    #     new_dict[xuexiaomingcheng].update({'cengci': '本科'})
                    # elif zhuan_ben == '专科':
                    #     new_dict[xuexiaomingcheng].update({'cengci': '专科'})
        if querymode == 'zhuanye':
            new_dict = {}
            for entry in result_data['jieguo']:
                zhaoshengzhuanye = entry['zhaoshengzhuanye']
                if zhaoshengzhuanye in new_dict:
                    new_dict[zhaoshengzhuanye]['data'].append(entry)
                else:
                    new_dict[zhaoshengzhuanye] = {
                        'data': [entry],
                    }
        return JsonResponse(new_dict)
