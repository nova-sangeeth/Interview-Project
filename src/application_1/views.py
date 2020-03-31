from django.shortcuts import render, redirect, HttpResponse
from .forms import usercreate, EditUserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash, get_user_model
from .table import UserTableList
from .forms import userprofile_form, customer_config_form


def welcome(request):

    return render(request, "dash.html")


def showthis(request):
    queryset = User.objects.all()
    all_users = UserTableList(queryset)
    return render(request, 'users_list.html', {'allusers': all_users})


def index(request):
    return render(request, "index.html")


def register(request):
    form = usercreate
    profile_form = userprofile_form
    if request.method == "POST":
        form = usercreate(request.POST)
        profile_form = userprofile_form(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            auth_login(request, user)
            return redirect("welcome")

    else:
        form = usercreate()
        profile_form = userprofile_form()
    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})


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


def edit_profile(request):
    if request.method == 'POST':
        # form = EditProfileForm(request.POST, instance=request.user)
        # form = EditProfileForm(instance=request.user.userprofile)
        form = EditUserForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
        else:
            return redirect('welcome')
    else:
        form = EditUserForm(instance=request.user)
        return render(request, 'edit_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('welcome'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'change_password.html', {'form': form})


def customer_config(request):
    form = customer_config_form
    if request.method == "POST":
        form = customer_config_form(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect("welcome")
    else:
        form = customer_config_form()
    return render(request, 'Home.html', {'form': form})
