from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError  # この行を追加
from django.contrib.auth import authenticate, login

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'login.html', {'error': 'このユーザーは既に登録されています！'})
    return render(request, 'login.html', {'some': 100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'context': 'logged in'})
            ...
        else:
            return render(request, 'login.html', {'context': 'not logged in'})
    
    return render(request, 'login.html', {'context': 'get method'}) 