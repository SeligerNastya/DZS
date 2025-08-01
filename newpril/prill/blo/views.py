from django.shortcuts import render, get_object_or_404
from .models import Blo

def blos(request):
    blos = Blo.objects.order_by('-date')
    return  render(request, "blo/blo.html", {"blos": blos})

def detail(request, blo_id):
    blo = get_object_or_404(Blo, pk=blo_id)
    return render(request, 'blo/details.html', {'blo': blo})
