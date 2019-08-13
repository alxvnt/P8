from django.urls import path
from product import views

urlpatterns = [
    path('search/<str:prod>/', views.prod_view, name='search'),
    path('result/<str:prod>/', views.prod_result, name='result'),
    path('validation/<str:prod>', views.save_product, name ='save_product'),
    path('details/<str:prod>/', views.prod_details, name='details'),
    path('ajouter_com/<str:prod>/', views.add_com, name='add_com'),
]