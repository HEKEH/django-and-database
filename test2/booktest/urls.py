from django.urls import path
from django.conf.urls import url,include
from . import views
from . import viewUtil
app_name ='booktest'
urlpatterns =[
    url('^$', views.index,name='index'),
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
    url('^temptest1$', views.temptest1),
    url('^index2$', views.index2),
    url('^user(\d+)$', views.user),
    url('^csrf1$', views.csrf1),
    url('^csrf2$', views.csrf2),
    url('^verifycode$', viewUtil.verifycode),
    url('^verifyTest1$', views.verifyTest1),
    url('^verifyTest2$', views.verifyTest2),
    url('^statictest$', views.staticTest),
    url(r'^myexp$',views.myExp),
    url(r'^uploadPic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle),
    url(r'^herolist/(\d*)/?$',views.herolist),
    url(r'^area/?$',views.area),
    url(r'^area/pro/?$',views.pro),
    url(r'^area/(\d+)/city/?$',views.city),
    url(r'^area/(\d+)/dis/?$', views.dis),
    url(r'^htmlEditor/?$', views.htmlEditor),
    url(r'^htmlEditorHander/?$', views.htmlEditorHander),

]