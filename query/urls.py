from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index),
    path('cx_danzhao/', views.cx_danzhao),
    path('query/danzhao/zhuanye/', views.query_danzhao_processing.as_view()),
    path('query/danzhao/xuexiao/', views.query_danzhao_processing.as_view()),
    path('days/', views.daojishi),
    path('cx_benkefenshuxian/', views.cx_benkefenshuxian),
    path('cx_zhuankefenshuxian/', views.cx_zhuankefenshuxian),
    path('query/fenshuxian/', views.query_fenshuxian_processing.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]
