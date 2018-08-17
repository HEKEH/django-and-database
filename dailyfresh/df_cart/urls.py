from django.conf.urls import url
from . import views


app_name ='df_cart'

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^add_(\d+)_(\d+)$', views.add),
]