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
    rows = Cloth.objects.all()
    context = {
        'rows':rows
    }
    return render(request, "shop.html", context)

def shopSingle(request, id):
    row = Cloth.objects.get(id = id)
    images = ItemImages.objects.filter(clothObject = row)
    # вам нужно отобразить конкретный товар на странице shop-single.html
    # мы это делали когда работали с пустым шаблоном в другом мини проекте

    context = {
        'cloth':row,
        'images':images
    }

    return render(request, "shop-single.html", context)

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



