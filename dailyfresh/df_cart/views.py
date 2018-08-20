# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
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
    carts_count = ucarts.count()
    if request.is_ajax():
        return JsonResponse({'count': carts_count})
    context = {
        'title': '购物车',
        'carts': ucarts,
        'carts_count': carts_count,
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
        return JsonResponse({'count': count1, 'cid': cart.id})
    return redirect('/cart')


@user_decorator.login
def edit(request, cid, count):
    if request.is_ajax():
        count = int(count)
        cart0 = CartInfo.objects.get(id=int(cid))
        cart0.count = count
        cart0.save()
    return HttpResponse()

@user_decorator.login
def delete(request, cid):
    if request.is_ajax():
        try:
            CartInfo.objects.get(id=int(cid)).delete()
            return JsonResponse({'ok': 1})
        except Exception as e:
            return JsonResponse({'ok': 0})
    return HttpResponse()
