from django.shortcuts import render, redirect
from app_purbeurre.models import Product, SavedSubstitute, User, Commentary, CommentaryProduct
from django.contrib.auth.decorators import login_required
from app_purbeurre.forms import SearchForm
from product.forms import CommentaryForm
from datetime import date


def prod_view(request, prod):
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
    list_prod = Product.objects.filter(
        nutrition_grade__range = ('d', 'e'), name__icontains = prod)
    return render(request, 'product/search.html', locals())


def prod_result(request, prod):
    """
        Get all the potential sub
        for the product in param
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
    research = Product.objects.get(name= prod)

    list_prod = Product.objects.filter(
        nutrition_grade__range = ('a', 'b'), category = research.category)
    return render(request, 'product/result.html',  locals())


@login_required
def save_product(request, prod):
    """
        Save a product in db if it's not
        already save
    """
    prod_to_save = Product.objects.get(name=prod)
    current_user = request.user

    if request.method == 'POST':

        fav1 = SavedSubstitute.objects.filter(substitute=prod_to_save,user=current_user.id)
        if not fav1:
            fav2 = SavedSubstitute(substitute=prod_to_save, user=current_user.id)
            fav2.save()
            result = 1

        return render(request, 'product/validation.html', locals())

    return render(request, 'app_purbeurre/index.html', locals())


def prod_details(request, prod):
    """
        Get the product in parameter
        and return the template which
        print product's information
    """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            prod = form.cleaned_data['research']
            return redirect('/' + prod + '/')
        else:
            form = SearchForm()
            com = CommentaryForm()
    else:
        form = SearchForm()
        com = CommentaryForm()
    details_prod = Product.objects.get(name=prod)
    com_prod = CommentaryProduct.objects.filter(prod=details_prod)
    return render(request, 'product/details.html', locals())


@login_required
def add_com(request, prod):

    current_user = request.user
    prod_to_com = Product.objects.get(name=prod)
    if request.method == 'POST':
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.cleaned_data["commentary"]
            com1 = (current_user.username + " : " + commentary)
            com = Commentary(com=com1, com_date=date.today())
            com.save()
            print(com)
            com_prod = CommentaryProduct(prod=prod_to_com, com=com)
            com_prod.save()
    return redirect('/details/' + prod + '/')
