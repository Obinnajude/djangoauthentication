from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "account/index.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        newuser = User.objects.create_user(username, email, password1)
        newuser.first_name = fname
        newuser.last_name = lname
        newuser.save()
        messages.success(request, 'User created successfully')
        return redirect('logon')
    else:
        return render(request, "account/register.html")


def logon(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        myuser = authenticate(request, username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            return redirect('authview')
        else:
            return redirect('index')
    else:
        return render(request, "account/login.html")


def logoutuser(request):
    logout(request)
    return redirect('index')


@login_required(login_url='logon')
def authview(request):
    return render(request, "account/authview.html")
