from django.shortcuts import render, redirect, HttpResponse
from .forms import usercreate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


def welcome(request):
    return render(request, "dash.html")


def index(request):
    return render(request, "index.html")


def register(request):
    form = usercreate
    if request.method == "POST":
        form = usercreate(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("welcome")

    else:
        form = usercreate()
    return render(request, 'register.html', {'form': form})


def login(request):
    form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('welcome')
        else:
            return render(request, 'incorrect_password.html')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout(request):
    # if request.method == "POST":
    auth_logout(request)
    # else:
    return render(request, 'logout.html')
