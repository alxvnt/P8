from django.urls import path
from app_purbeurre import views

urlpatterns = [
    path('accueil', views.home, name='index'),
    path('mentions_legales/', views.mentions, name="mentions_legales"),
    path('enregistrement/', views.register, name="enregistrement"),
]