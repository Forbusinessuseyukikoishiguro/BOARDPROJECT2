from django.contrib import admin
from .models import BoardModel  # このインポート文を追加

# Register your models here.
admin.site.register(BoardModel)