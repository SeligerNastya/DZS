from django.urls import path
from . import views

urlpatterns = [
    path('', views.us, name="us" ),
    path('uss/<str:pk>/', views.uss, name="uss"),
    path('home/', views.home, name="home" ),
    path('home/<str:pk>/', views.homes, name="homes" ),

]
