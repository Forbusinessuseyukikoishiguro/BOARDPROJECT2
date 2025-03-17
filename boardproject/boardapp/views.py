from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupfunc(request):
   # object_list = User.objects.all()
   
    object = User.objects.get(username = 'tanaka')
    print(object.email)
                
    
    if request.method == "POST":
        print("this is post method")
    else:
        print("this is not post method")
    return render(request, 'signup.html',{})