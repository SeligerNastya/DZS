from django.urls import path
from . import views

urlpatterns = [
    path('', views.blos, name="blos"),
    path('<int:blo_id>/', views.detail, name ="detail"),

]