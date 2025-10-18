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

def homes(request):
    hom = Home.objects.all()
    contex ={
        'home': hom
    }
    return render(request, "us/home.html", contex)

def home(request, hom):
    home_obj = Home.objects.get(id=hom)


    return  render(request, 'us/single-home.html', {'homes': home_obj})


def attraction(request):
    attr = Attractions.objects.all()
    contex = {
        'attractions': attr
    }
    return render(request, "us/attractions.html", contex)
def attractions(request, attr):
    attraction_obj = Attractions.objects.get(id=attr)
    context = {
        'title': attraction_obj.title,
        'attraction': attraction_obj,
        }
    return render(request, 'us/single-attractions.html', context)
