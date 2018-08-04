from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete = False)
    def create(cls, btitle, bpub_time):
        b = BookInfo()
        b.bpub_time = bpub_time
        b.btitle = btitle
        b.bread = 0
        b.bcomment = 0
        b.isDelete = 0
        return b

class BookInfo(models.Model):
    btitle = models.CharField(max_length = 20)
    bpub_time = models.DateTimeField()
    bread = models.IntegerField(default = 0)
    bcomment = models.IntegerField(default = 0)
    isDelete = models.BooleanField(default = False)
    class Meta:
        db_table = 'bookinfo'
    books1 = models.Manager()
    books2 = BookInfoManager()  #repalce objects
    def __str__(self):
        return self.btitle

    @classmethod
    def create(cls, btitle, bpub_time):
        b = BookInfo()
        b.bpub_time = bpub_time
        b.btitle = btitle
        b.bread = 0
        b.bcomment = 0
        b.isDelete = 0
        return b



class HeroInfo(models.Model):
    hname = models.CharField(max_length = 20)
    hgender = models.BooleanField(default = True)
    hcontent = models.CharField('武功', max_length = 200)
    isDelete = models.BooleanField(default = 0)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    def hbooktitle(self):
        return self.hbook.btitle

    gender.short_description = '性别'
    hbooktitle.short_description = '书名'
    #hcontent.short_description = '武功'

