from django.shortcuts import render
from django.http import request, HttpResponse
from .models import *

import sys
sys.path.append('../')
from df_user.models import *
from df_goods.models import *
from df_cart.models import *
from datetime import datetime
from decimal import Decimal
from django.db import transaction

from django.http import JsonResponse
from df_user import user_decorator
# Create your views here.
'''
事务：一旦操作失败则全部回退
1、创建订单对象
2、判断商品的库存
3、创建详单对象
4、修改商品库存
5、删除购物车
'''
@user_decorator.login
def order(request):
    uid = request.session.get('user_id')
    user = UserInfo.objects.get(id=uid)
    if request.GET.get('c_id'):
        carts_list = [CartInfo.objects.get(id=cid) for cid in request.GET.getlist('c_id')];
    else:
        carts_list = [CartInfo.objects.get(goods_id=gid) for gid in request.GET.getlist('g_id')];
    context = {
        'title': '订单',
        'carts_list': carts_list,
        'user': user,
    }
    return render(request, 'df_order/place_order.html', context)

@transaction.atomic()
@user_decorator.login
def order_handle(request):
    tran_id = transaction.savepoint()
    try:
        order = OrderInfo()

        uid = request.session.get('user_id')
        order.user_id = uid

        now = datetime.now()
        order.date = now
        order.oid = int('%s%d'%(now.strftime('%y%m%d%H%M%S'), uid))

        post = request.POST
        order.ototal = Decimal(post.get('ototal'))
        order.address = post.get('oaddress')
        order.save()

        cart_ids = post.getlist('cart_ids[]')

        for cid in cart_ids:
            cart = CartInfo.objects.get(id=cid)
            goods = cart.goods
            count = cart.count
            if int(goods.gstock) >= int(count):
                goods.gstock -= count

                order_detail = OrderDetailInfo()
                order_detail.goods = goods
                order_detail.price = goods.gprice
                order_detail.count = count
                order_detail.order_id = order.oid
                order_detail.save()

                goods.save()

                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                # 返回json供前台提示失败
                return JsonResponse({'status': 2})

    except Exception as e:
        print('==================%s' % e)
        transaction.savepoint_rollback(tran_id)

    # finally:
    #     transaction.savepoint_commit(tran_id)
    return JsonResponse({'status': 1})