from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import SearchForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,
                                            email = email,
                                            last_name=last_name,
                                            first_name=first_name,
                                            password=password
                                            )
            return redirect('/')
        else:
            pass
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', locals())


def connexion(request):

    error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = LoginForm()
    return render(request, 'users/login.html', locals())


def deconnexion(request):
    logout(request)
    return HttpResponseRedirect('/')

def mon_compte(request):

    return render(request, 'users/mon_compte.html')