from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length = 20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    bname = models.CharField(max_length = 10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length = 1000)
    hbook = models.ForeignKey(BookInfo, on_delete = models.CASCADE)
    def __str__(self):
        return self.bname
    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'