from django.shortcuts import render
from app_purbeurre.models import Product, SavedSubstitute, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


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

        #fav1 = get_object_or_404(SavedSubstitute, substitute=prod_to_save,user=current_user.id)

        #if not fav1:
        fav2 = SavedSubstitute(substitute=prod_to_save, user=current_user.id)
        fav2.save()
        print(fav2.substitute)

        return render(request, 'product/validation.html', locals())

    return render(request, 'app_purbeurre/index.html', locals())


def prod_details(request, prod):
    details_prod = Product.objects.get(name=prod)
    return render(request, 'product/details.html', locals())
