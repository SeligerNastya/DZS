from django.shortcuts import render
from .models import Us

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
    return render(request, "home/home.html")
