from django.shortcuts import render
from app_purbeurre.models import Product
from django.contrib.auth.decorators import login_required


def prod_view(request, prod):


    list_prod = Product.objects.filter(
        nutrition_grade__range = ('d', 'e'), name__icontains = prod)
    return render(request, 'product/search.html', {'list_prod': list_prod})

def prod_result(request, prod):

    research = Product.objects.get(name= prod)

    list_prod = Product.objects.filter(
        nutrition_grade__range = ('a', 'b'), category = research.category)
    return render(request, 'product/result.html',  locals())


def toast(request):

    list_prod = Product.objects.all()
    return render(request, 'product/toast.html', {'list_prod': list_prod})


@login_required
def save_product(request, prod):
    pass


def prod_details(request, prod):
    details_prod = Product.objects.get(name=prod)
    return render(request, 'product/details.html', locals())