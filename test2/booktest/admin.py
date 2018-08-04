from django.contrib import admin

# Register your models here.
from .models import *

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
#列表页
    list_display = ['pk', 'btitle','bpub_time']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    # fieldsets = [
    #     ('base', {'fields':['btitle']}),
    #     ('super', {'fields':['bpub_time']})
    # ]
    inline = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'hname', 'gender', 'hbooktitle', 'hcontent']



admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
