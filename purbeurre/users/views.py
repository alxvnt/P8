from django.shortcuts import render, redirect
from .forms import SearchForm, RegisterForm
from django.contrib.auth.models import User


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

def login(request):

    return render(request, 'users/login.html')