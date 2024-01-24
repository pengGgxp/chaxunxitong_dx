import json

from django.test import TestCase

# Create your tests here.
d = {'querymode': 'xuexiao',
     'jieguo': '{"zhaoshengxinxi": [{"id": 1, "xuexiaomingcheng_id": 1, "zhuanyemingcheng": "数字媒体", "zhaoshengjihua": 10, "xuefei": 4800.0, "zhaoshengleixing": "\\u5355\\u72ec\\u62db\\u751f", "xingzhi": "\\u4e13\\u79d1", "nianfen": 2024, "zhuanyeleibie": "\\u8ba1\\u7b97\\u673a", "kebaozhiyuansl": 20, "kaoshineirong": "\\u5927\\u5927", "kaoshifangshi": "\\u7ebf\\u4e0b", "beizhu": "\\u6c11\\u529e", "xuexiaomingcheng": "\\u5317\\u4eac\\u5927\\u5b66"}, {"id": 5, "xuexiaomingcheng_id": 2, "zhuanyemingcheng": "\\u5927\\u8428\\u8fbe", "zhaoshengjihua": 10, "xuefei": 8888.0, "zhaoshengleixing": "\\u5355\\u72ec\\u62db\\u751f", "xingzhi": "\\u672c\\u79d1", "nianfen": 2024, "zhuanyeleibie": "\\u963f\\u8fbe\\u963f\\u8fbe\\u5927\\u5927\\u7684", "kebaozhiyuansl": 3000, "kaoshineirong": "\\u53d1\\u5927\\u6c34\\u53d1\\u751f", "kaoshifangshi": "\\u7ebf\\u4e0b", "beizhu": "\\u516c\\u529e", "xuexiaomingcheng": "\\u6e05\\u534e\\u5927\\u5b66"}, {"id": 6, "xuexiaomingcheng_id": 2, "zhuanyemingcheng": "\\u5927\\u5927\\u5927", "zhaoshengjihua": 10, "xuefei": 888.0, "zhaoshengleixing": "\\u5355\\u72ec\\u62db\\u751f", "xingzhi": "\\u672c\\u79d1", "nianfen": 2024, "zhuanyeleibie": "\\u8ba1\\u7b97\\u673a", "kebaozhiyuansl": 20, "kaoshineirong": "1011", "kaoshifangshi": "\\u7ebf\\u4e0b", "beizhu": "\\u516c\\u529e", "xuexiaomingcheng": "\\u6e05\\u534e\\u5927\\u5b66"}]}'}

result = json.loads(d['jieguo'])

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

print(json.dumps(new_dict, indent=4))
