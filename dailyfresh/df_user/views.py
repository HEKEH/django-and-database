#coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from hashlib import sha1
from . import user_decorator

import sys
sys.path.append('../')
from df_goods.models import *

# Create your views here.
def register(request):
    context = {'title': '注册'}
    return render(request, 'df_user/register.html', context)


def register_handle(request):
    # 接受用户输入
    post = request.POST
    uname = post.get("user_name")
    upwd = post.get("pwd")
    upwd2 = post.get("cpwd")
    uemail = post.get("email")

    # 判断两次密码
    if upwd != upwd2:
        return redirect('user/register')

    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()

    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    # 注册成功，转向登录页
    return redirect('user/login')

def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'uname': uname, 'error_name': 0, 'error_pwd': 0,}
    return render(request, 'df_user/login.html', context)

def login_handle(request):
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')
    isRemembered = post.get('isRemembered', 0)
    users = UserInfo.objects.filter(uname=uname)

    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('current_url','/user/info')
            red = HttpResponseRedirect(url)
            red.delete_cookie('current_url')
            if isRemembered != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = users[0].uname
            return red
        else:
            context = {'title': '用户登录', 'uname': uname, 'error_name': 0, 'error_pwd': 1, 'upwd': upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录', 'uname': uname, 'error_name': 1, 'error_pwd': 0, 'upwd': upwd}
        return render(request, 'df_user/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/goods/index')


@user_decorator.login
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    gids = request.COOKIES.get('goodsids')
    gids_lst = gids.split(',')
    if '' in gids_lst:
        gids_lst.remove('')
    recent_click_glist = []
    for gid in gids_lst:
        recent_click_glist.append(GoodsInfo.objects.get(id=int(gid)))
    context = {
        'title': '用户中心',
        'user_email': user_email,
        'user_name': request.session['user_name'],
        'recent_click_glist': recent_click_glist,
    }

    return render(request, 'df_user/user_center_info.html', context)

@user_decorator.login
def order(request):
    context = {'title': '用户中心'}
    return render(request, 'df_user/user_center_order.html', context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.uaddress = post.get('uaddress')
        user.ureceiver = post.get('ureceiver')
        user.upostcode = post.get('upostcode')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title':'用户中心', 'user': user}
    return render(request, 'df_user/user_center_site.html' , context)





