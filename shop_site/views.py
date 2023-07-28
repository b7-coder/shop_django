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

from django.core.paginator import Paginator

def shop(request):
    allrows = Cloth.objects.all()
    rows = Paginator(allrows, 3)
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    else:
        page = 1
    context = {
            'rows':rows.page(page),
            'paginator': rows,
            'page':page
        }
    return render(request, "shop.html", context)

def shopSingle(request, id):
    row = Cloth.objects.get(id = id)
    images = ItemImages.objects.filter(clothObject = row)
    
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



