from django.shortcuts import render
from .models import Us, Home,Attractions

def us(request):
    u = Us.objects.all()
    contex = {
        'us': u
    }
    return render(request, "us/us.html", contex)

def uss(request, u):
    us_obj = Us.objects.get(id=u)
    return render(request, 'us/single-us.html', {'uss': us_obj})

def home(request):
    hom = Home.objects.all()
    contex ={
        'home': hom
    }
    return render(request, "us/home.html", contex)

def homes(request, hom):
    home_obj = Home.objects.get(id = hom)


    return  render(request, 'us/single-home.html', {'homes': home_obj})


def attractions(request):
    a = Attractions.objects.all()
    contex = {
        'attractions': a
    }
    return render(request, "us/attractions.html", contex)
def attraction(request, a):
    attraction_obj = Attractions.objects.get(id=a)
    context = {
        'title': attraction_obj.title,
        'attraction': attraction_obj,
        }
    return render(request, 'us/single-attraction.html', context)
