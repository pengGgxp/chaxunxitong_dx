from django.db.models import Sum

from .models import Page, Images


class PageViewCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            total_view_count = Page.objects.aggregate(Sum('view_count'))['view_count__sum']
        except:
            total_view_count = 1
        request.total_view_count = total_view_count

        response = self.get_response(request)

        if response.status_code == 200 and request.method == "GET":
            try:
                page = Page.objects.get(url=request.path_info)
                page.increase_view_count()
            except Page.DoesNotExist:
                Page.objects.create(url=request.path_info, view_count=1)
        return response

class setlogo_waterfillMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        request.logo_image = Images.objects.filter(is_logo=True).first()
        request.watermark_image = Images.objects.filter(is_watermark=True).first()
        response = self.get_response(request)

        return response
