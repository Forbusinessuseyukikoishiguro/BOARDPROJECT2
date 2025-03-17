from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = User.objects.create_user(username, '', password)
        
    return render(request, 'signup.html', {'some': 100})