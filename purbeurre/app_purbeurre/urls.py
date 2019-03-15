from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home, name='index'),
    path('mentions_legales/', views.mentions, name="mentions_legales"),
]