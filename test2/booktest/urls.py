from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns =[
    path('', views.index),
    url('^(?P<p1>\d+)/(?P<p3>\d+)/(?P<p2>\d+)$', views.detail),
    url('^gettest1$', views.getTest1),
    url('^gettest2$', views.getTest2),
    url('^gettest3$', views.getTest3),
    url('^posttest1$', views.postTest1),
    url('^posttest2$', views.postTest2),
    url('^cookietest$', views.cookieTest),
    url('^redtest1$', views.redTest1),
    url('^redtest2$', views.redTest2),
    url('^session1$', views.session1),
    url('^session2$', views.session2),
]