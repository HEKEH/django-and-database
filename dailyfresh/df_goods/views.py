from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, Page

# Create your views here.


def index(request):
    #拿到各分类最新和最热的4条数据
    typelist = TypeInfo.objects.all()
    context = {'title': '首页', 'typelist': typelist, 'type_new': [],  'type_hot': []}
    for i in range(len(typelist)):
        gtype = typelist[i]
        type_new = gtype.goodsinfo_set.filter(isDelete=False).order_by('-id')[0:4]
        type_hot = gtype.goodsinfo_set.filter(isDelete=False).order_by('-gclick')[0:4]
        context['type_new'].append(type_new)
        context['type_hot'].append(type_hot)
    return render(request, 'df_goods/index.html', context)

def list(request, tid, pindex, sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':
        goods_list = typeinfo.goodsinfo_set.order_by('-id')
    elif sort == '2':
        goods_list = typeinfo.goodsinfo_set.order_by('gprice')
    elif sort == '3':
        goods_list = typeinfo.goodsinfo_set.order_by('-gclick')
    pagenator = Paginator(goods_list, 10)
    page = pagenator.page(int(pindex))
    context = {
        'title': typeinfo.ttitle,
        'page': page,
        'pagenator': pagenator,
        'tid': tid,
        'sort':sort,
        'pindex':pindex,
        'news': news,
    }
    return render(request, 'df_goods/list.html', context)

def detail(request, gid):
    goodsinfo = GoodsInfo.objects.get(pk=int(gid))
    goodsinfo.gclick += 1
    goodsinfo.save()

    typelist = TypeInfo.objects.all()
    news = goodsinfo.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title': goodsinfo.gtitle,
        'typelist': typelist,
        'goods': goodsinfo,
        'news': news,
        'id': gid,
    }
    response = render(request, 'df_goods/detail.html', context)

    #浏览记录
    goodsids = request.COOKIES.get('goodsids', '')
    goodsid = str(gid)
    if goodsids != '':
        goodsids_lst = goodsids.split(',')
        if goodsids_lst.count(goodsid) >= 1:
            goodsids_lst.remove(goodsid)
        goodsids_lst.insert(0, goodsid)
        if len(goodsids_lst) >= 6:
            del goodsids_lst[5]
        goodsids = ','.join(goodsids_lst)
    else:
        goodsids = goodsid
    response.set_cookie('goodsids', goodsids)
    return response