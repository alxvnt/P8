from django.shortcuts import render
from app_purbeurre.models import Product, SavedSubstitute, User
from django.contrib.auth.decorators import login_required


def prod_view(request, prod):
    """
    Get all the product which
    contains the parameter in their name
    """
    list_prod = Product.objects.filter(
        nutrition_grade__range = ('d', 'e'), name__icontains = prod)
    return render(request, 'product/search.html', {'list_prod': list_prod})


def prod_result(request, prod):
    """
        Get all the potential sub
        for the product in param
    """
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
    details_prod = Product.objects.get(name=prod)
    return render(request, 'product/details.html', locals())
