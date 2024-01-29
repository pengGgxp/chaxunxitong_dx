from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index),
    path('cx/', views.cx),
    path('cx/query/zhuanye/', views.query_processing.as_view()),
    path('cx/query/xuexiao/', views.query_processing.as_view()),
    path('days/', views.daojishi),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]
