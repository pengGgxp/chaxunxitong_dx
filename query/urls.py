from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cx/', views.cx),
    path('cx/query/zhuanye/', views.query_processing.as_view()),
    path('cx/query/xuexiao/', views.query_processing.as_view()),
    path('days/',views.daojishi)
]
