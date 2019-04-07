from django.shortcuts import render, redirect
from .forms import SearchForm, HomeSearchForm


def home(request):
    """  Return the homepage """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        form_body = HomeSearchForm(request.POST)
        if form.is_valid():
            prod = form.cleaned_data['research']
            return redirect('search/' + prod + '/')
        else:
            form = SearchForm()
            form_body = HomeSearchForm()
    else:
        form = SearchForm()
        form_body = HomeSearchForm()
    return render(request, 'app_purbeurre/index.html', locals())


def mentions(request):
    """  Return the  Legal notice"""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            prod = form.cleaned_data['research']
            return redirect('/' + prod + '/')
        else:
            form = SearchForm()
    else:
        form = SearchForm()
    return render(request, 'app_purbeurre/mentions_legales.html', locals())


