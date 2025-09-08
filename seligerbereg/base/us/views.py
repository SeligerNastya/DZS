from django.shortcuts import render
from .models import Us, Home

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
    homs = Home.objects.all()
    contex ={
        'home': homs
    }
    return render(request, "us/home.html", contex)
def homes(request, hom):
    home_obj = Home.objects.get(id = hom)


    return  render(request, 'us/single-home.html', {'us': home_obj})
