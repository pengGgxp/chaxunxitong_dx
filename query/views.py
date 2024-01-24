import encodings
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q, Count
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from django.views import View

from query.models import zhaoshengxinxi, xuexiaoinfo


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cx(request):
    context = {
        'sc': xuexiaoinfo.objects.all(),
        'leixing': zhaoshengxinxi.objects.values_list('zhaoshengleixing', flat=True).distinct(),
        'nian': zhaoshengxinxi.objects.values_list('nianfen', flat=True).distinct(),
        'banxuexingzhi': xuexiaoinfo.objects.values_list('beizhu', flat=True).distinct(),
        'fangshi': zhaoshengxinxi.objects.values_list('kaoshifangshi', flat=True).distinct(),
    }

    return render(request, 'query/zhuankexuexiaocx.html', context=context)


class query_processing(View):
    @staticmethod
    def post(request):
        querymode = request.POST.get('querymode')
        zhaoshengleixing = request.POST.get('zhaoshengleixing')
        nianfen = request.POST.get('nianfen')
        banxuexingzhi = request.POST.getlist('banxuexingzhi[]')
        kaoshifangshi = request.POST.getlist('kaoshifangshi[]')
        mingcheng = request.POST.get('mingcheng')

        result_data = {}
        queryset = zhaoshengxinxi.objects.all()
        queryset = queryset.select_related('xuexiaomingcheng')
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

        tmp = list(queryset.all().values())
        for entry in tmp:
            beizhu = xuexiaoinfo.objects.get(id=entry.get('xuexiaomingcheng_id')).beizhu
            xuexiaomingcheng = xuexiaoinfo.objects.get(id=entry.get('xuexiaomingcheng_id')).xuexiaomingcheng
            entry.update({'beizhu': beizhu, 'xuexiaomingcheng': xuexiaomingcheng})

        result_data['jieguo'] = json.dumps({'zhaoshengxinxi': tmp}, cls=DjangoJSONEncoder)
        if querymode=='xuexiao':
            result = json.loads(result_data['jieguo'])

            new_dict = {}

            for entry in result['zhaoshengxinxi']:
                xuexiaomingcheng_id = entry['xuexiaomingcheng_id']

                if xuexiaomingcheng_id in new_dict:
                    new_dict[xuexiaomingcheng_id]['data'].append(entry)
                else:
                    new_dict[xuexiaomingcheng_id] = {
                        'xuexiaomingcheng': entry['xuexiaomingcheng'],
                        'beizhu': entry['beizhu'],
                        'data': [entry],
                    }
            return JsonResponse(new_dict)

        if querymode=='zhuanye':
            result = json.loads(result_data['jieguo'])

            new_dict = {}
            for entry in result['zhaoshengxinxi']:
                zhuanyemingcheng = entry['zhuanyemingcheng']

                if zhuanyemingcheng in new_dict:
                    new_dict[zhuanyemingcheng]['data'].append(entry)
                else:
                    new_dict[zhuanyemingcheng] = {
                        'xuexiaomingcheng': entry['xuexiaomingcheng'],
                        'beizhu': entry['beizhu'],
                        'data': [entry],
                    }
            return JsonResponse(new_dict)
