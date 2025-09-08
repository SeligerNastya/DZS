from django.urls import path
from . import views

urlpatterns = [
    path('', views.us, name="us" ),
    path('uss/<str:u>/', views.uss, name="uss"),
    path('home/', views.home, name="home" ),
    path('us/<str:hom>/', views.homes, name="us" ),

]
