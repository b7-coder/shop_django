from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    rows = Slider.objects.all()
    slidersCount = len(rows)
    context = {
        'rows' : rows,
        'buttons': range(slidersCount)
    }

    return render(request, "index.html", context)

def about(request):
    rows = Brands.objects.all()
    context = {
        'rows' : rows,
    }
    return render(request, "about.html",context)

def contact(request):
    return render(request, "contact.html")

def shop(request):
    return render(request, "shop.html")

def shopSingle(request):
    return render(request, "shop-single.html")



