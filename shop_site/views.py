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
    rows = BrandsLogo.objects.all()
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

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def contactSaveFunc(request):

    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    newRow = Contacts.objects.create(name = name, email = email, subject=subject, message=message)
    newRow.save()

    return contact(request)



