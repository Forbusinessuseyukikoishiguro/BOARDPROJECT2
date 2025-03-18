from django.db import models

# Create your models here.

class BoardModel(models.Model):  # models.Modelを継承する必要があります
    title = models.CharField(max_length=100)  # 'charField'ではなく'CharField'が正しい
    content = models.TextField()
    author = models.CharField(max_length=100)  # 'charField'ではなく'CharField'が正しい
    snsimage = models.ImageField(upload_to='')
    good = models.IntegerField()  # デフォルト値を設定すると便利
    read = models.IntegerField()  # デフォルト値を設定すると便利
    readtext = models.TextField()  # 空を許可する場合はblank=Trueを指定