from django.urls import path
from . import views

urlpatterns = [
    path('', views.us, name="us" ),
]
