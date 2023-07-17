from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()

class Brands(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()

class Contacts(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

class BrandsLogo(models.Model):
    firstImage = models.ImageField()
    secondImage = models.ImageField()
    thirdImage = models.ImageField()
    fourthImage = models.ImageField()
