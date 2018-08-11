from .models import *
from django.shortcuts import render,redirect
from django.db.models import Max,F,Q
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.conf import settings
import os
from django.core.paginator import *

# Create your views here.
def index(request):
    #list = BookInfo.books2.filter(heroinfo__hcontent__contains='八')
    #list = BookInfo.books2.filter(bread__gte=20)
    #list = BookInfo.books2.filter(bread__lt = F('bcomment'))
    list = BookInfo.books2.filter(~Q(bread = 0))
    #Max1 = BookInfo.books2.aggregate(Max('bpub_time'))
    context = {'list' : list,
               #'Max1' : Max1
               }
    return render(request, 'booktest/index.html', context)

def detail(request, p1, p2, p3):
    #return HttpResponse(request.GET)
    return HttpResponse('year:%s, month:%s, day:%s'%(p1, p2, p3))

def getTest1(request):
    return render(request, 'booktest/getTest1.html')

def getTest2(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    context = {
        'a': a,
        'b': b,
        'c': c,
    }
    return render(request, 'booktest/getTest2.html',context)

def getTest3(request):
    list1 = request.GET.getlist('a')
    context = {
        'list': list1,
    }
    return render(request, 'booktest/getTest3.html',context)

def postTest1(request):
    return render(request, 'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST.get('uname')
    ugender = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    context = {
        "uname": uname,
        "ugender": ugender,
        "uhobby": uhobby,
    }
    return render(request, 'booktest/postTest2.html', context)

def cookieTest(request):
    response = HttpResponse()
    if 't1' in request.COOKIES:
        response.write('<h1>' + request.COOKIES['t1'] + '</h1>')
    else:
        response.set_cookie('t1','abc')
    return response

def redTest1(request):
    return HttpResponseRedirect('redtest2')
    #or return redirect('redtest2')

def redTest2(request):
    return HttpResponse('转向')

def session1(request):
    uname = request.session.get('uname','新用户')
    context = {'uname' : uname}
    return render(request, 'booktest/session1.html', context)

def session2(request):
    uname = request.POST.get('uname')
    request.session['uname'] = uname
    return redirect('/booktest/session1')

def temptest1(request):
    list = HeroInfo.objects.all()
    context = {'list':list}
    return render(request,'booktest/temptest1.html',context)

def index2(request):
    return render(request,'booktest/index2.html')

def user(request, id):
    return render(request,"booktest/user%s.html"%id)
    # return render(request, 'booktest/user2.html',
    #               {
    #                   't1': '<h1>hello</h1>'
    #               })

def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST["uname"]
    context={"uname":uname}
    return render(request, 'booktest/csrf2.html', context)

def verifyTest1(request):
    return render(request, 'booktest/verifyTest1.html')

def verifyTest2(request):
    vc = request.POST['vc']
    if vc.upper() == request.session['verifycode']:
        return HttpResponse("OK")
    else:
        return HttpResponse("No")

#静态文件处理
def staticTest(request):
    return render(request, "booktest/staticTest.html")

#中间件
def myExp(request):
    a1=int("abc")
    return HttpResponse("hello")

#上传图片
def uploadPic(request):
    return render(request,'booktest/uploadPic.html')

def uploadHandle(request):
    if request.method == "POST":
        f1 = request.FILES['pic1']
        fname = os.path.join(settings.MEDIA_ROOT,f1.name)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        return HttpResponse("<img src='/static/media/%s'/>"%f1.name)
    else:
        return HttpResponse("error")

#进行分页练习
def herolist(request, pindex):
    if pindex == '':
        pindex = '1'
    list = HeroInfo.objects.all()
    paginator = Paginator(list, 5) #每页5条,页码从1开始
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'booktest/herolist.html', context)

#省市区选择
def area(request):
    return render(request, 'booktest/area.html')

def pro(request):
    data = AreaInfo.objects.filter(parea__isnull = True)
    lst = []
    for a in data:
        lst.append([a.id, a.title])
    return JsonResponse({'data':lst})
    #结果是
    #{"data": [[120000, "\u5929\u6d25\u5e02"], [130000, "\u6cb3\u5317\u7701"], [140000, "\u5c71\u897f\u7701"], [150000, "\u5185\u8499\u53e4\u81ea\u6cbb\u533a"], [210000, "\u8fbd\u5b81\u7701"], [220000, "\u5409\u6797\u7701"], [230000, "\u9ed1\u9f99\u6c5f\u7701"], [310000, "\u4e0a\u6d77\u5e02"], [320000, "\u6c5f\u82cf\u7701"], [330000, "\u6d59\u6c5f\u7701"], [340000, "\u5b89\u5fbd\u7701"], [341402, "\u5c45\u5de2\u533a"], [350000, "\u798f\u5efa\u7701"], [360000, "\u6c5f\u897f\u7701"], [370000, "\u5c71\u4e1c\u7701"], [410000, "\u6cb3\u5357\u7701"], [420000, "\u6e56\u5317\u7701"], [430000, "\u6e56\u5357\u7701"], [440000, "\u5e7f\u4e1c\u7701"], [450000, "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"], [460000, "\u6d77\u5357\u7701"], [500000, "\u91cd\u5e86\u5e02"], [510000, "\u56db\u5ddd\u7701"], [520000, "\u8d35\u5dde\u7701"], [530000, "\u4e91\u5357\u7701"], [540000, "\u897f\u85cf\u81ea\u6cbb\u533a"], [610000, "\u9655\u897f\u7701"], [620000, "\u7518\u8083\u7701"], [630000, "\u9752\u6d77\u7701"], [640000, "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a"], [650000, "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a"], [990000, "\u65b0\u7586\u5efa\u8bbe\u5175\u56e2"]]}

def city(request,id):
    data = AreaInfo.objects.filter(parea_id = id)
    lst = []
    for a in data:
        lst.append({'id':a.id, 'title':a.title})
    return JsonResponse({'data':lst})

def dis(request,id):
    data = AreaInfo.objects.filter(parea_id = id)
    lst = []
    for a in data:
        lst.append({'id':a.id, 'title':a.title})
    return JsonResponse({'data':lst})

def htmlEditor(request):
    return render(request, 'booktest/htmlEditor.html')

def htmlEditorHander(request):
    html = request.POST['hcontent']
    test1 = tinymceTest1()
    test1.content = html
    test1.save()
    return HttpResponse(test1.content)
