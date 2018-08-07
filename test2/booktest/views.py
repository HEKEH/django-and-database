from django.shortcuts import render,redirect
from django.db.models import Max,F,Q
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
from .models import *
def index(request):
    #list = BookInfo.books2.filter(heroinfo__hcontent__contains='八')
    #list = BookInfo.books2.filter(bread__gte=20)
    #list = BookInfo.books2.filter(bread__lt = F('bcomment'))
    list = BookInfo.books2.filter(Q(bread__gte=12) | Q(bcomment__gte=34))
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