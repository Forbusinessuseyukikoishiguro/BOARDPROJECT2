from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import BoardModel  # ドットの後にスペースを削除
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('login')  # サインアップ成功後にログインページへリダイレクト
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています！'})
    return render(request, 'signup.html', {'some': 100})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST.get('username')  # POSTの値を取得するメソッドを統一
        password = request.POST.get('password')  # POSTの値を取得するメソッドを統一
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')  # ログイン成功後にリストページへリダイレクト
        else:
            return render(request, 'login.html', {'error': 'ユーザー名またはパスワードが正しくありません'})
    
    return render(request, 'login.html')


def listfunc(request):
    object_list = BoardModel.objects.all()  # 'object' から 'objects' に修正（重要）
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object': object})