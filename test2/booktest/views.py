from django.shortcuts import render
from django.db.models import Max,F,Q
from django.http import HttpResponse

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