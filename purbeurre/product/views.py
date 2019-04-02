from django.shortcuts import render
from app_purbeurre.models import Product, SavedSubstitute, User
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


@login_required
def save_product(request, prod):

    prod_to_save = Product.objects.get(name=prod)
    current_user = request.user

    if request.method == 'POST':

        fav = SavedSubstitute(substitute=prod_to_save,user=current_user.id)
        if not fav:
            fav.save()
        return render(request, 'product/validation.html', locals())

    return render(request, 'app_purbeurre/index.html', locals())


def prod_details(request, prod):
    details_prod = Product.objects.get(name=prod)
    return render(request, 'product/details.html', locals())
