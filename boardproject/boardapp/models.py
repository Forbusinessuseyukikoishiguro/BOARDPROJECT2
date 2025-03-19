from django.db import models

# Create your models here.

class BoardModel(models.Model):  # models.Modelを継承する必要があります
    title = models.CharField(max_length=100)  # 'charField'ではなく'CharField'が正しい
    content = models.TextField()
    author = models.CharField(max_length=100)  # 'charField'ではなく'CharField'が正しい
    snsimage = models.ImageField(upload_to='')
    good = models.IntegerField(default=0, null=True,blank=True)  # このフィールドが必要
    read = models.IntegerField(null=True,blank=True)  # デフォルト値を設定すると便利
    readtext = models.TextField( null=True,blank=True)  # 空を許可する場合はblank=Trueを指定