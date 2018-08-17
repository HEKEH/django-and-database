from django.db import models
from tinymce import HTMLField
# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='static/df_goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gunit = models.CharField(max_length=20, default='500g')
    gclick = models.IntegerField(default=0)
    gdescription = models.CharField(max_length=100)
    gstock = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE)
    grecommend = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gtitle