from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError  # この行を追加

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています！'})
    return render(request, 'signup.html', {'some': 100})