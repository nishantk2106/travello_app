from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method == 'POST' :
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        password1= request.POST['password1']
        email= request.POST['email']
        password2= request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
        else:
            print('password not matching............')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')