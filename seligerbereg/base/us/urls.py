from django.urls import path
from . import views

urlpatterns = [
    path('', views.us, name="us" ),
    path('uss/<str:u>/', views.uss, name="uss"),
    path('homes/', views.homes, name="homes" ),
    path('us/<str:hom>/', views.home, name="home" ),
    path('attractions/', views.attraction, name="attraction" ),

]
