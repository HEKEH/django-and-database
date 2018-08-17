from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import sys
sys.path.append('../')
from df_user.models import *
from df_goods.models import *

from df_user import user_decorator

@user_decorator.login
def cart(request):
    uid = request.session.get('user_id')
    ucarts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title': '购物车',
        'carts': ucarts,
        'carts_count': ucarts.count(),
    }
    return render(request, 'df_cart/cart.html', context)

@user_decorator.login
def add(request, gid, count):
    uid = request.session.get('user_id')
    gid = int(gid)
    count = int(count)
    carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)

    if len(carts) >= 1:
        cart = carts[0]
        cart.count += count
    else:
        cart = CartInfo()
        cart.count = count
        cart.user_id = uid
        cart.goods_id = gid
    cart.save()
    if request.is_ajax():
        count1 = CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({'count': count1})
    return redirect('/cart')
