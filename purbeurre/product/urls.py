from django.urls import path
from product import views

urlpatterns = [
    path('search/<str:prod>/', views.prod_view, name='search'),
    path('result/<str:prod>/', views.prod_result, name='result'),
    path('toast/', views.toast, name ='toast'),
    path('details/<str:prod>/', views.prod_details, name='details'),
]