from django.shortcuts import render

# Create your views here.
from .models import *
def index(request):
    list = BookInfo.books2.filter(heroinfo__hcontent__contains='八')
    context = {'list' : list}
    return render(request, 'booktest/index.html', context)

