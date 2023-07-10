from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    rows = Slider.objects.all()

    context = {
        'rows' : rows
    }

    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def shop(request):
    return render(request, "shop.html")

def shopSingle(request):
    return render(request, "shop-single.html")



