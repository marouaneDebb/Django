from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')

    

    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['First name']
        last_name = request.POST['last name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        

        user = User.objects.create_user(last_name = last_name,first_name = first_name,password = password1,email = email,username = username)
        user.save();
        return redirect('login')
    else:
        return render(request, 'register.html')

