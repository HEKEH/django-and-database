from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns =[
    path('', views.index),
    url('^(?P<p1>\d+)/(?P<p3>\d+)/(?P<p2>\d+)$', views.detail),
]