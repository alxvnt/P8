from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return render(request, 'app_purbeurre/index.html')

def mentions(request):

    return render (request, 'app_purbeurre/mentions_legales.html')
