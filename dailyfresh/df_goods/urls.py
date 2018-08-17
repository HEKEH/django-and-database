from django.conf.urls import url
from . import views


app_name ='df_goods'

urlpatterns = [
    url(r'^index/*$', views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/*$', views.list),
    url(r'^detail/(\d+)/*$', views.detail),
]