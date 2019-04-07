from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import SearchForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app_purbeurre.models import SavedSubstitute, Product


def register(request):
    """
        Get all the data from
        the register form and create
        an object from the user's models
    """
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
    """
        Connect the user
    """
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
    """
        Disconnect the user
    """
    logout(request)
    return HttpResponseRedirect('/')


def mon_compte(request):
    """
        Get all the product which
        contains the parameter in their name
    """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            prod = form.cleaned_data['research']
            return redirect('/' + prod + '/')
        else:
            form = SearchForm()
    else:
        form = SearchForm()
    return render(request, 'users/mon_compte.html', locals())


def fav(request):
    """
        Get all the product which
        have been save by the user
    """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            prod = form.cleaned_data['research']
            return redirect('/' + prod + '/')
        else:
            form = SearchForm()
    else:
        form = SearchForm()

    current_user = request.user
    fav = SavedSubstitute.objects.filter(user=current_user.id)

    return render(request, 'users/mes_aliments.html', locals())


def delete_product(request):
    """
        Remove the select product
    """
    if request.method == 'POST':

        prod_name = request.POST.get('delete_prod')
        prod_to_delete = Product.objects.get(name=prod_name)
        current_user = request.user
        SavedSubstitute.objects.get(substitute=prod_to_delete, user=current_user.id).delete()
        return render(request, 'users/suppression.html', locals())

    return render(request, 'users/suppression.html', locals())
