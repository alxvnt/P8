from django.urls import path
from app_purbeurre import views

urlpatterns = [
    path('', views.home, name='index'),
    path('mentions_legales/', views.mentions, name="mentions_legales"),

]