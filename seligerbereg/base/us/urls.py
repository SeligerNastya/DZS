from django.urls import path
from . import views

urlpatterns = [
    path('', views.us, name="us" ),
    path('uss/<str:u>/', views.uss, name="uss"),
    path('homes/', views.homes, name="homes" ),
    path('home/<str:hom>/', views.home, name="home" ),
    path('attraction/', views.attraction, name="attraction" ),
    path('attractions/<int:attr>/', views.attractions, name="attractions"),
    path('contact/', views.contact, name="contact")

]
