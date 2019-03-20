from django.urls import path
from users import views

urlpatterns = [
    path('enregistrement/', views.register, name="enregistrement"),
    path('connexion', views.login, name="connexion"),

]